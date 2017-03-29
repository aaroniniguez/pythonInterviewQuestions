class A(object):
    def calc(self):
        return 7
class B(object): 
    def calc(self):
        return 6
class C(A,B):
    pass
c = C()
print c.calc()
