#!/usr/bin/python
import unittest

def get_magic_index_slow(A):
	'''
		Returns A magic index i in a sorted array A of distinct ints, -1 if it doesn't exist.
		Magic Index is an index such that A[i] = i.Count of how many possible ways the child can run up the stairs	
		Time Complexity: O(n)
		Space Complexity: O(1)
	'''

	for i in range(len(A)):
		if A[i] == i:
			return i
	return -1

def get_magic_index_better(A):
	'''
		Returns A magic index i in a sorted array A of distinct ints, -1 if it doesn't exist.
		Magic Index is an index such that A[i] = i.Count of how many possible ways the child can run up the stairs	
		Time Complexity: O(log n)
		Space Complexity: O(1)
	'''

	def helper(A, low, high):
		mid_ind = (low + high) / 2
		mid_el = A[mid_ind]
		if mid_el == mid_ind:
			return mid_ind
		elif mid_ind == 0 or mid_ind == len(A)-1:
			return -1
		elif mid_el < mid_ind:
			#look right			
			return helper(A, mid_ind, high)
		elif mid_el > mid_ind:
			#look left
			return helper(A, low, mid_ind)

	return helper(A, 0, len(A))
	
class Test_Magic_Index(unittest.TestCase):

	def test_basic_cases_slow(self):
		self.assertEquals(0, get_magic_index_slow([0,1,2,3,4,5]))
		self.assertEquals(2, get_magic_index_slow([-2,0,2]))
		self.assertEquals(-1, get_magic_index_slow([-1,-2,-3]))

	def test_basic_cases_better(self):
		self.assertEquals(0, get_magic_index_better([0,2,4,6,8,10]))
		self.assertEquals(2, get_magic_index_better([-2,0,2]))
		self.assertEquals(-1, get_magic_index_better([-1,-2,-3]))

if __name__ == '__main__':
	unittest.main()