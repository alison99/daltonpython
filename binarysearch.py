#Give an algorithm to return the location of a given element, if it is present
#(a sorted list - like phonebook)

A = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	while first <=last and not found:
		midpoint = (first+last)/2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint -1
			else: first = midpoint + 1
	return found

print binarySearch(A, 55)

def binarySearchrec(alist, item):
	if len(alist)==0:
		return False
	else:
		midpoint = len(alist)/2
		if alist[midpoint]== item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist[:midpoint], item)
			else:
				return binarySearch(alist[midpoint+1:], item)

print binarySearchrec(A, 55)

#give an algorithm to sort a list of number
A = [25, 16, 71, 3, 14, 82, 9, 11, 29, 64]