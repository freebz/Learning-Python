from decotools import tracer

class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):       # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)     # onCall이 giveRaise를 기억

    @tracer
    def lastName(self):                 # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10) # Runs onCall(sue, .10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())   # onCall(bob)을 실행, lastName을 기억
