# When Object is destroyed based on some condition then destructor is called. It is used to clean up the resources used by the object. 

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Connected to the database for")
    def info(self):
        print(self.name,self.age)
    def __del__(self):
        print("Disconnected from the database for")
def generate_student():
    s1=student("BMK",15)
    s1.info()
generate_student()

# While we are working on Project after obj is created then specific method is called and it works.
# After that if we are not using that obj then it is destroyed and destructor is called to clean up the resources used by the object.
