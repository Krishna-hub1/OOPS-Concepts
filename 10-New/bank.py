class IntCalculator:
    def __init__(self, name, principal, rate, time):
        self.name = name
        self.principal = principal
        self.rate = rate
        self.time = time
    def info(self):
        print(self.name, self.principal, self.rate, self.time)
    def simple_interest(self):
        return (self.principal * self.rate * self.time) / 100
