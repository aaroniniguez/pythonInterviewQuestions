mylist = [4]
myelement = 4
def binSearch(mylist,myelement):
    top = len(mylist)-1
    bottom = 0
    middle = top/2
    while bottom <= top:
        if myelement > mylist[middle]:
            bottom = middle+1
            middle = (top-bottom)/2 + bottom
        elif myelement < mylist[middle]:
            top = middle-1
            middle = (top-bottom)/2 +bottom
        else:
            return middle

print binSearch(mylist,myelement)
