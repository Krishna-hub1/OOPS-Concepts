# Changing the behaviour of base class method in derived class is called method overriding. 

class A:
    def display(self):
        print("This is method 1 from class A.")
    def info(self):
        print("This is info method from class A.")

class B(A):
    def show(self):
        print("This is method 1 from class B.")
    def info(self):
        print("This is info method from class B.")
obj=B()
obj.display()
obj.info()

# Here, we have a base class A with a method info(). 
# The derived class B overrides the info() method of class A. When we call obj.info(), it executes the overridden method in class B.