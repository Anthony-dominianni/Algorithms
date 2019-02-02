import math

#Return the number of times a given number n is contained in a sorted list L
def findRepeats(L, n):

	lo = 0
	hi = len(L) - 1

	count = 0
	while lo <= hi:
		mid = math.floor((hi + lo)/ 2)
		if L[mid] < n:
			lo = mid + 1
		elif L[mid] > n:
			hi = mid - 1
		else: 
			count+=1
			rightIdx = mid + 1
			leftIdx = mid - 1
			while leftIdx >= 0:
				if L[leftIdx] == n:
					count+=1
					leftIdx-=1
				else:
					break
			while rightIdx < hi:
				if L[rightIdx] == n:
					count+=1
					rightIdx+=1
				else: 
					break
			break		
	return count

L1 = [1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19]
L2 = [3, 5, 6, 8, 8, 9]

print(findRepeats(L1, 1))
print(findRepeats(L2, 4))