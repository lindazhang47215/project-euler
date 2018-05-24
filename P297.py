# Problem 297

import numpy as np

F = []
A = []

F.append(1)
F.append(2)
A.append(0)
A.append(1)
A.append(2)

searchrange_i = 100
max_n = 100

# Construct the list of Fibonacci numbers F
for i in range(2,searchrange_i,1):
	new_F = F[i-2]+ F[i-1]
	F.append(new_F)
	if new_F > max_n and F[-2] <= max_n:
		max_i = i-1
		max_F = F[-2]

# Construct the list of A which is the sum of Z(n) for n between 0 and F_i-1
for i in range(3,searchrange_i,1):
	A_i = A[i-2] + A[i-1] + F[i-2]
	A.append(A_i)	
	print(i, " ", F[i], " ", A[-1])

# Recursively calculate T(n), where T(n) = A[i] + T(residual) + residual, and F[i] is the biggest Fib number below n
def T(n, A, F):
	max_ind=0
	res = 0
	if n == 0:
		return 0

	for i in range(len(F)-2, -1, -1):
		
		if F[i] <= n and F[i+1] > n:
			max_ind = i
			res = n - F[max_ind]
			break
	return A[max_ind] + T(res, A, F) + res


total = T(10 ** 17, A, F) 

print (total)