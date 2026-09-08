# Hiding Implementation Details from the user is called Abstraction. In Python, we can achieve abstraction by using abstract classes and methods.
#  An abstract class is a class that cannot be instantiated and is meant to be subclassed by other classes.

from abc import ABC,abstractmethod
class calculation(ABC):
    def __init__(self,a,b):
        self.a=a
    @abstractmethod
    def isprime(self):
        pass
    @abstractmethod
    def isperfect(self):
        pass
    def info(self):
        print("It is Implementation of abstract class")

# Here It is an abstract class with two abstract methods is_Prime() and is_Perfect().
# it is main Method we can show it to the user.
