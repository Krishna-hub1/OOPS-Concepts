from base import calculation
class main_calculation(calculation):
    def __init__(self, a, b):
        super().__init__(a, b)

    def isprime(self):
        for d in range(2, self.a):
            if self.a % d == 0:
                return False
        else:
            return True
    def isperfect(self):
        s=0
        for d in range(1,self.a//2+1):
            if self.a%d==0:
                s+=d
            if s==self.a:
                return True
            else:
                return False

# Here It is a main logic behind the code that we cannot show it to the user.
# It is Just a small logic but when you are working on a big project you can hide the implementation details from the user and show only the main method to the user like this.
