# Single Inheritance allows a child class to inherit properties and methods from a single base class.
# The main idea Inheritance is code reusability. 

class A:
    def method1(self):
        print("This is method 1 from class A.")
    
class B(A):
    def method2(self):
        print("This is method 2 from class B.")
obj = B() # Calling method from base class A
obj.method1()  # Calling method from base class A
obj.method2()  # Calling method from derived class B

# Here, class B inherits from class A, allowing it to access method1() from class A while also having its own method2().
# Here we Created object for B but we can access method1() from class A because of inheritance.