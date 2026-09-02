# static methods are utility methods that do not depend on class or instance variables.
# Static methods are defined using the @staticmethod decorator.
# These process data which is not related to class but process individual data.
class Student:

    # Class variables
    institute = "VCube"
    std_fees = []

    def __init__(self, name, age, m1, m2, fee):
        # Instance variables
        self.name = name
        self.age = age
        self.Physics_Marks = m1
        self.Math_Marks = m2

        # Adding each student's fee to the class variable
        Student.std_fees.append(fee)

    # Instance method
    def info(self):
        return self.name, self.age

    # Instance method
    def getaverage(self):
        return (self.Physics_Marks + self.Math_Marks) // 2

    # Static method
    @staticmethod
    def isprime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
obj = Student("Balu", 22, 80, 90, 1000)
# Calling the static method using the class
is_prime = Student.isprime(17)
print("Is 17 a prime number?", is_prime)

# Here, isprime() is a static method that checks if a number is prime. 
# It does not depend on any instance or class variables, so it is defined as a static method. 
# We can call it using the class name without creating an instance of the class.