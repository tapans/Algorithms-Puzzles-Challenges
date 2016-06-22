#!/usr/bin/python
import unittest

def triple_step(n, memo={}):
	'''
		Returns Count of how many possible ways the child can run up the stairs
		Context: Child is running up a stairacase with n steps 
			and can hop either 1 step, 2 steps or 3 steps at a time
		Time Complexity: O(n)
		Space Complexity: O(n)
	'''

	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		hop_3_down = memo[n-3] if n-3 in memo else triple_step(n - 3, memo)
		hop_2_down = memo[n-2] if n-2 in memo else triple_step(n - 2, memo)
		hope_1_down = memo[n-1] if n-1 in memo else triple_step(n - 1, memo)
		memo[n] = sum([hop_3_down, hop_2_down, hope_1_down])		
		return memo[n]

class Test_Tripe_Step(unittest.TestCase):

	def test_regular_case(self):
		self.assertEquals(1, triple_step(1))
		self.assertEquals(2, triple_step(2))
		self.assertEquals(4, triple_step(3))
		self.assertEquals(7, triple_step(4))
		self.assertEquals(13, triple_step(5))

if __name__ == '__main__':
	unittest.main()