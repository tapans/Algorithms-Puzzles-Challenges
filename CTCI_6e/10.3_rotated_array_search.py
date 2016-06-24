#!/usr/bin/python
import unittest

def rotated_array_search(A, k):
	'''
		Finds index of element k in a sorted array A that has been rotated an unknown # of times
		Time Complexity: O()
		Space Complexity: O()
	'''

	def rotated_array_search_helper(A,k,index_tracker):
		n = len(A)
		mid = n / 2		
		if A[mid] == k:			
			return index_tracker
		elif n == 1:
			return -1
		elif A[mid - 1] >= A[0]:
			new_mid = mid / 2
			if k > A[mid - 1] or k < A[0]:
				index_tracker += new_mid
				return rotated_array_search_helper(A[mid + 1:], k, index_tracker)
			else:
				index_tracker -= new_mid
				return rotated_array_search_helper(A[0:mid], k, index_tracker)
		elif A[n - 1] >= A[mid + 1]:
			new_mid = mid / 2
			if k > A[n - 1] or k < A[mid + 1]:
				index_tracker -= new_mid
				return rotated_array_search_helper(A[0:mid], k, index_tracker)
			else:
				index_tracker += new_mid
				return rotated_array_search_helper(A[mid + 1:], k, index_tracker)

	n = len(A)
	if n == 0:
		return -1
	else:
		index_tracker = n / 2
		return rotated_array_search_helper(A,k, index_tracker)

class Test_Rotated_Array_Search(unittest.TestCase):

	def test_basic(self):
		self.assertEquals(8, rotated_array_search([15,16,19,20,25,1,3,4,5,6,10,14], 5))
		self.assertEquals(4, rotated_array_search([6,7,8,9,10,1,2,3,4,5,10], 10))

if __name__ == '__main__':
	unittest.main()