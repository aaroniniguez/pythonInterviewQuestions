#get nth value in fibonacci sequence
class fib:
    def __init__(self):
        self.savedVals = {}
    def getNth(self,n):
        if n ==0:
            return 0
        if n == 1:
            return 1
        if n in self.savedVals:
            return self.savedVals[n]
        else:
            result =self.getNth(n-1)+self.getNth(n-2)
            self.savedVals[n] = result
            return result
myfib = fib()
print myfib.getNth(90)
