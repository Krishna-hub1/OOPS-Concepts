# static methods are utility methods that do not depend on class or instance variables.
# Static methods are defined using the @staticmethod decorator.
# These process data which is not related to class but process individual data.
class Student:

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Static method
    @staticmethod
    def isprime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
obj = Student("Balu", 22)
# Calling the static method using the class
is_prime = Student.isprime(17)
print("Is 17 a prime number?", is_prime)

# Here, isprime() is a static method that checks if a number is prime. 
# It does not depend on any instance or class variables, so it is defined as a static method. 
# We can call it using the class name without creating an instance of the class.