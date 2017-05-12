#Can you give an algorithm to multiply two matrices? Translate into a Python function.

A = [[1,4,6]]
B = [[2,3],[5,8],[7,9]]
C = [[0]*len(B[0])]*len(A)

#columns of A = [A[0]]
#rows of A = len(A)

print len(A[0])


def mmult(A, B):
	if len(A[0]) != len(B):
		print "columns of first must equal rows of second!"
		return
	else:
		for i in range(len(A)):
			for j in range(len(B[0])):
				#take a dot product
				for k in range(len(A[0])):
					C[i][j] += A[i][k]*B[k][j]
	return C

def dot(x,y):
	total = 0
	for i in range(len(x)):
		total = total + x[i]*y[i]
	return total

def mult(A, B):
	if(len(A[0])==len(B)):
		i=0
		while i<len(A):
			j=0
			while j<len(B[0]):
				k=0
				while k<len(B):
					C[i][j] += A[i][k]*B[k][j]
					k+=1
				j+=1
			i+=1
	return C

print("let's multiply!")
print mult(A,B)
print mmult(A,B)