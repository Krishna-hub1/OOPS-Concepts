from new_bank import NewCalculator
object = NewCalculator('Ram',1000,5,2)
object.info()
amount=object.simple_interest()
print("Simple Interest is:",amount)
compound_amount=object.compound_interest()
print("Compound Interest is:",compound_amount)