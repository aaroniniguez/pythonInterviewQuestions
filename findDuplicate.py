mylist = [1,2,3,3,4]
def getdup(mylist):
    prev = 0
    for i in mylist:
        if i == prev:
            return i
        else:
            prev = i
    return False
print getdup(mylist)
