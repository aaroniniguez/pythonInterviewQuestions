files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print files["Input.txt"]
mydict = {}
for i in files:
        print files[i]
        if files[i] not in mydict:
            mydict[files[i]] = [i]
        else:
            mydict[files[i]].append(i)
print mydict

