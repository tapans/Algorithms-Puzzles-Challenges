#!/usr/bin/python
import unittest

def get_toh_steps(n):
	'''
		Return num of steps needed to move n disks from tower A to tower C
		in accordance to the tower of hanoi puzzle
		Time Complexity: O(n)
		Space Complexity: O(1)
	'''

	if n == 1:
		return 1
	else:
		return 1 + 2*get_toh_steps(n - 1)

	
class Test_Tower_of_Hanoi(unittest.TestCase):

	def test_basic_cases(self):
		self.assertEquals(1, get_toh_steps(1))
		self.assertEquals(3, get_toh_steps(2))
		self.assertEquals(7, get_toh_steps(3))
		self.assertEquals(15, get_toh_steps(4))		

if __name__ == '__main__':
	unittest.main()