listdemo = [1, 2.0, "three", (2**2)]
print listdemo[2]
print type(listdemo)

emptylist = []
print str(len(emptylist))
print str(len(listdemo))

#deletes item from list
del listdemo[0]
print listdemo[0]

if 'three' in listdemo:
	print "found you"

print listdemo[-1]
#first element is always 0 - can't refer to it as -4
#can use negative indices for others

emptylist.append("hi my name is")
superlist = emptylist + listdemo
i=0
while i < len(superlist):
	print superlist[i]
	i += 1
print superlist

superlist[2] = "element"
print superlist