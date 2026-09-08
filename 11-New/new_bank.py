from bank import IntCalculator
class NewCalculator(IntCalculator):
    def compound_interest(self):
        return self.principal * (1 + self.rate / 100) ** self.time
    