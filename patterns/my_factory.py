
from abc import abstractmethod # abc is abstract base class

# here is a top-level abstract class
class Animal():
    @abstractmethod
    def make_a_noise(self):
        pass # abstract, so no actual body

# here are some concrete classes
class Dog(Animal):
    def make_a_noise(self):
        print('woof')
class Cat(Animal):
    def make_a_noise(self):
        print('miaow')
class Bat(Animal):
    def make_a_noise(self):
        print('______')
class Lion(Animal):
    def make_a_noise(self):
        print('roar')

# a factory to create our animals
class CreatureFactory():
    '''this is a single-point of access for our creatures'''
    def make_sound(self, obj): # here we deal with one outcome - there could be many
        return eval(obj)().make_a_noise() # this returns a call to the method of the requested creature

if __name__ == '__main__':
    '''exercise our code'''
    cf = CreatureFactory() # we now have an instance of our factory
    creature = input('which creature? ') # we ought to validate this!!!
    cf.make_sound(creature)