def value_exists(A,val):
	exists = False
	for i in range(len(A)):
		if A[i] == val:
			exists = True
			break
	return exists

A = ["A","B","C"]
val = "j"

print value_exists(A,val)