
mylist = [1,2,3,4]
def find_repeat(numbers):
    myset = set()
    for i in numbers:
        if i in myset:
            return i
        else:
            myset.add(i)
    raise Exception("no duplicates")

    
print find_repeat(mylist)
