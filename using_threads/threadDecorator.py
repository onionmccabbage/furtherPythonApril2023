# we can write decorators to apply to any function and make it thread-safe
from threading import Lock

lock = Lock()

def lock_a_method(meth):
    '''this can be used to decorate any methopd that needs to be thread safe (i.e. use locks)'''
    if getattr(meth, '__is_locked', False):
        raise TypeError(f'Method {meth} is already locked')
    def locked_method(self, *args, **kwargs):
        # we cannot use 'with' since Lock does not implement __enter__ or __exit__
        # with self.__lock: # 'with' will release the lock when done
        #     return meth(self, *args, **kwargs)
        lock.acquire()
        result = meth(self, *args, **kwargs)
        lock.release()
        return result
    lock_a_method.__name__ = f'Locked Method {meth.__name__}'
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, method_names, lock_factory):
    '''iterate over all the methods of a class making each thread safe'''
    init = cls.__init__ # take a copy of the current __init__ for the class
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock_factory
    cls.__init__ = new_init # our decorated class now has a replacement __init__ method
    # iterate over the methods of the class
    for methodN in method_names:
        old_meth = getattr(cls, methodN)
        new_meth = lock_a_method(old_meth)
        setattr(cls, methodN, new_meth) # replace the original method with the new version
    return cls

# here is a decorator to make selected class methods thread safe
def lock_a_class(method_names, lock_factory):
    return lambda cls: make_thread_safe(cls, method_names, lock_factory)

# some arbitrary code
@lock_a_class(['add', 'remove'], Lock)
class MyClass(set): # here our class inherits from the 'set' class
    def __init__(self, new_set): # since we extend the 'set' class, we need to provide a set
        set.__init__(self, new_set) # call the initializer of the 'set' class
    @lock_a_method # here we apply a decorator to make this method thread-safe
    def someMethod(self):
        print(f'Here is an arbitrary method')
    # def add(self):
    #     print('This would be an add method')
    # def remove(self):
    #     print('This would be a remove method')
        
if __name__ == '__main__':
    ''''''
    initial_set = {4,3,2}
    s = MyClass(initial_set)
    s.add('apples')
    s.remove(4)
    print(s)
    # see if 'someMethod' is locked
    print(s.someMethod.__is_locked) # True
    print(s.add.__is_locked) # True
    print(s.remove.__is_locked) # True