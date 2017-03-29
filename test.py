class Calculator(object):
    def __repr__(self):
        return "this is a calculator Calculator" 
    def __init__(self):
        self.current = 0
    def add(self,amount):
        self.current += amount
    def getCurrent(self):
        return self.current

mycalc = Calculator()
mycalc.add(23)
mycalc.add(10)
print mycalc.getCurrent()
class Calculator1(Calculator):
    def add(self,amount):
        self.current += amount*2
mycalc1 = Calculator1()
mycalc1.add(19)
mycalc1.add(1)
print mycalc1.getCurrent()
print mycalc
