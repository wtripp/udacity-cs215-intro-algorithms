def merge(A,B):
	if not A:
		return B
	if not B:
		return A
	if A[0] < B[0]:
		return [A[0]] + merge(A[1:], B)
	else:
		return [B[0]] + merge(A, B[1:])

A = [2,3,4,6,7,8]
B = [1,3,5,9]

		
def merge_slow(A,B):
	if not A:
		return B
	if not B:
		return A
	else:
		new_list = []
		for n in A:
			new_list.append(n)
		for n in B:
			new_list.append(n)
		return new_list

print merge(A,B)
print merge_slow(A,B)	
		
		
		
		