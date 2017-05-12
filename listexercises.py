#1. write a loop that traverses:
#['spam!', 1, ['brie', 'roquefort', 'pol le veq'],[1, 2, 3]]
#and prints the length of each element. what happens if you send an integer to len?
#change 1 to 'one' and run your solution again
newlist = ['spam!', 1, ['brie', 'roquefort', 'pol le veq'],[1, 2, 3]]
i = 0
while i < len(newlist) :
	#print len(newlist[i])
	i+=1
#gets error: object of type 'int' has no len()

i=0
while i < len(newlist) :
	if type(newlist[i])== int: newlist[i] = str(newlist[i])
	print len(newlist[i])
	i+=1
print newlist


newlist = ['spam!', 'one', ['brie', 'roquefort', 'pol le veq'],[1, 2, 3]]
i = 0
while i < len(newlist) :
	print len(newlist[i])
	i+=1


#2. what will be the output of the following program?
this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print "test 1: %s" % (this is that)
that = this
print "test 2: %s" % (this is that)