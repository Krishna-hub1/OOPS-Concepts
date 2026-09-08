# Message Passing in Python is used to transfer the data from one object to another object.
# data shared in terms of messages between objects. 

class A:
    def __init__(self, m):
        self.m = m
class B:
    def is_prime(self, obj):
        for d in range(2, obj.m//2 + 1):
            if obj.m % d == 0:
                return False
            return True
obj1 = A(5)
obj2 = B()
result = obj2.is_prime(obj1)
print(result)
obj2.is_prime(obj1)
