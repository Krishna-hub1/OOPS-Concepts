# same piece of code can behave differently in different situations. based on object type respective method is called it is polymorphism. It is one of the important feature of object oriented programming.
import random
class Upi:
    def payment(self):
        print("UPI Payment")
class Card:
    def payment(self):
        print("Card Payment")
class NetBanking:
    def payment(self):
        print("Net Banking Payment")
upi=Upi()
card=Card()
netbanking=NetBanking()
random.shuffle([upi,card,netbanking])
for obj in [upi,card,netbanking]:
    obj.payment()

"""
This is an example of polymorphism. The same method name 'payment' is used in different classes, 
but the payment method implementation is different based on the object type.
it is also called duck typing.
"""