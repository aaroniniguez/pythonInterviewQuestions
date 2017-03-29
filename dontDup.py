def fib_recursive(n):
    if n < 0:
        raise IndexError("index was negative ")

    if n in [0,1]:
        return n
    print "computing fib_recursive(%i)" %n
    return fib_recursive(n-1)+fib_recursive(n-2)
#fib_recursive(100)

class Fibber:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n< 0:
            raise Exception("number n cannot be negative")

        elif n in [0, 1]:
            return n
        if n in self.memo:
            print "grabbing memo[%i]" % n
            return self.memo[n]
        print "computing fib(%i)" % n
        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result
        return result
print Fibber().fib(100)

