#!/usr/bin/python
import unittest

def get_subsets(A):
	'''
		Return list of all subsets of list a
		According to set theory, empty set and set itself are subsets of any sets
		Complexity: O(n*2^n)
	'''

	def union(el, A):
		subsets = [s for s in A]
		for s in A:
			subsets.append(s + [el])
		return subsets

	num_els = len(A)
	if num_els == 0:
		return [[]]
	else:
		return union(A[0], get_subsets(A[1:]))

	
class Test_Power_Set(unittest.TestCase):

	def test_basic_cases(self):
		self.assertEquals(1, len(get_subsets([])))
		self.assertEquals(2, len(get_subsets([1])))
		self.assertEquals(4, len(get_subsets([1,2])))
		self.assertEquals(8, len(get_subsets([1,2,3])))

if __name__ == '__main__':
	unittest.main()