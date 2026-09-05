# Multilevel Inheritance allows to use properties from Base class to child class and then to grandchild class. 
class Human:
    def __init__(self, name, acres):
        self.name = name
        self.acres = acres
    def info(self):
        print(self.name, self.acres)
class Farmer(Human):
    def __init__(self, name, acres, crop):
        super().__init__(name, acres)
        self.crop = crop
    def info(self):
        super().info()
        print(self.crop)
class Worker(Farmer):
    def __init__(self, name, acres, crop, job):
        super().__init__(name, acres, crop)
        self.job = job
    def info(self):
        super().info()
        print(self.job)
obj=Worker('Bmk',100,'Paddy','Agriculture Work')
obj.info()
"""
Here we got properties from the Human class to the Farmer and then farmer class to the worker class. it is called multi-level inheritance. 
super() method is used to call the parent class constructor and methods. In this example, we are able to access the properties of Human class in the Worker class.
"""