def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

var = raw_input("Please enter how many numbers in the fib sequence you want:\n")
mystring = [1,1]
if var == 1 : print 1
elif var ==2 : print 1
else:
    for i in range(3,int(var)+1):
            mystring.append(mystring[i-3]+mystring[i-2])
print " ".join(map(str, mystring))
