#!/usr/bin/python
import unittest

def sorted_merge(A, B):
	'''
		Merges B into A in sorted order and returns A (Both B and A are sorted arrays, & assume A has large enough buffer at end to hold B)
		Time Complexity: let n be len of A, m be len of B => O(n + m)
		Space Complexity: O(1)
	'''

	i = len(A) - 1
	j = len(B) - 1
	k = i + j + 1

	#b/c a is assumed to have large enough buffer at end to hold B
	[A.append(0) for x in range(j+1)]

	while j >= 0:
		if i >= 0 and A[i] > B[j]:
			A[k] = A[i]
			i -= 1
		else:
			A[k] = B[j]
			j -= 1
		k -= 1
	return A

class Test_Sorted_Merge(unittest.TestCase):

	def test_basic(self):
		self.assertEquals([1,2,3,4,5,6,7], sorted_merge([1,3,5,7], [2,4,6]))
		self.assertEquals([2,4,5,6], sorted_merge([5], [2,4,6]))

if __name__ == '__main__':
	unittest.main()