# state is just the data we pass around
# we may need to react to changes in state

# some state changes are only permitted in certain cirumstances
# a laptop can go from OFF to ON but not from OFF to SLEEP or OFF to HYBERNATE
# we can go from ON to SLEEP or ON to HYBERNATE

class ComputerState():
    name='state'
    allowed = []  #this list will contain permitted states
    def switch(self, state):
        if state.name in self.allowed:
            print(f'Current state {self} switching to {state.name}')
            self.__class__ = state # make the state change
        else:
             print(f'Current state {self} cannot switch to {state.name}')
    # __str__ will ALWAYS be used by 'print'. wee override __str__ to provide our own print output
    def __str__(self):
        return self.name

class On(ComputerState):
      name = 'on'
      allowed = ['off', 'sleep', 'hybernate']

class Off(ComputerState):
      name = 'off'
      allowed = ['on']

class Sleep(ComputerState):
    name = 'sleep'
    allowed = ['on']

class Hybernate(ComputerState):
      name = 'hybernate'
      allowed = ['on']

class Computer():
     def __init__(self, model):
          self.model = model
          self.state = Off() # use the 'Off' class
     def change(self, change_to):
          self.state.switch(change_to)

def main():
     comp = Computer('MyLaptop')
     comp.change(On)
     comp.change(Off)
     comp.change(On)
     comp.change(Sleep)
     comp.change(On)
     comp.change(Hybernate)
     comp.change(On)
     comp.change(Off)
     comp.change(Hybernate)
     comp.change(Sleep)
     
if __name__ == '__main__':
     main()