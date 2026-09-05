# Hierarchical Inheritance allows multiple child classes to inherit properties and methods from a single base class.

class A:
    def method1(self):
        print("This is method 1 from class A.")

class B(A):
    def method2(self):
        print("This is method 2 from class B.")

class C(A):
    def method3(self):
        print("This is method 3 from class C.")

# Creating objects of classes B and C
objB = B()
objC = C()

# Calling methods
objB.method1()  # Inherited from class A
objB.method2()  # Defined in class B
objC.method1()  # Inherited from class A
objC.method3()  # Defined in class C

# Here, both classes B and C inherit from class A, allowing them to access method1() from class A while also having their own methods method2() and method3(), respectively
