import math

# Return the index of n in a sorted list L
def binSearch(L, n):

	if len(L) == 0:
		return 0

	hi = len(L) - 1
	lo = 0

	while lo <= hi:
		mid = math.floor((hi + lo) / 2)
		if L[mid] == n:
			return mid
		elif L[mid] > n:
			hi = mid
		else:
			lo = mid

	return None


L = [1, 2, 3, 4, 5, 8, 9, 10, 24, 56, 67, 89, 102, 345, 677, 2345, 23457, 23758]

num = binSearch(L, 10)

print(num)
