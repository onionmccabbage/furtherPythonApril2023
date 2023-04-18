# we can create a decorator which can be applied to any function to make that function lock safe
# i.e. threaded or not threaded, we can decorate ANY function to be safe when using shared resources
from threading import Lock # 'Lock' is a lock factory

lock = Lock()

# declare a custom decorator
def lock_a_method(meth):
    if getattr(meth, '__is_locked', False): # yes, False!!! see later
        raise TypeError(f'Method {meth} is already locked')
    def locked_method(self, *args, **kwargs):
        # with self.__lock: # 'with' will release the lock when done
        lock.acquire()
        result  = meth(self, *args, **kwargs)
        lock.release()
        return result
    lock_a_method.__name__ = f'Locked method {meth.__name__}'
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, method_names, lock_factory):
    init = cls.__init__ # take a copy of the existing init method
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock_factory
    cls.__init__ = new_init # our decorated class now has a new init method
    # iterate over all the class methods making each one thread-safe with lock
    for methodN in method_names:
        old_meth = getattr(cls, methodN)
        new_meth = lock_a_method(old_meth)
        setattr(cls, methodN, new_meth)
    return cls # return the modified version of the class

# we will use this function as a decorator, so the 'cls' will be whatever class is being decorated
def lock_a_class(method_names, lock_factory):
    return lambda cls: make_thread_safe(cls, method_names, lock_factory)

# this class (and it's methods) will be decorated with our decorators
@lock_a_class(['add', 'remove'], Lock) # apply our decorator to this class
class MyClass(set): # our class inherits from the 'set' class
    def __init__(self, new_set):
        set.__init__(self, new_set) # call the initializer of the 'set' class
        pass
    @lock_a_method # apply a lock to this method specifically
    def method_to_lock(self):
        print('this method needs to be thread safe via locks')
    # def add(self): # the 'set' class already has 'add' and 'remove' methods
    #     pass
    # def remove(self):
    #     pass

if __name__ == '__main__':
    my_set = {4, 2, 3}
    my_set.add(9)
    print(my_set)
    class_inst = MyClass(my_set)
    class_inst.add(0)
    print(class_inst.add.__is_locked) # True
    print(class_inst.method_to_lock.__is_locked) # True