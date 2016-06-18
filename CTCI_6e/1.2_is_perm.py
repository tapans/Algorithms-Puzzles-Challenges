#!/usr/bin/python
import unittest

def is_perm(s1, s2):
	'''
		Returns True if a string is a permutation of other. False o/w
		Time Complexity: O(len(s1) + len(s2))
		Space Complexity: O(len(s1))
	'''

	s_len = len(s1)
	if (s_len != len(s2)):
		return False
	else:
		char_counts = {}
		for c in s1:
			if c in char_counts:
				char_counts[c] += 1
			else:
				char_counts[c] = 1
		for c in s2:
			if c not in char_counts:
				return False
			else:
				char_counts[c] -= 1
		for c in char_counts:
			if char_counts[c] != 0:
				return False
		return True


class Test_Is_Perm(unittest.TestCase):

	def test_perm_case(self):
		self.assertTrue(is_perm("incest", "insect"))
		self.assertTrue(is_perm("asdf", "sadf"))

	def test_not_perm_case(self):
		self.assertFalse(is_perm("incest", "incast"))
		self.assertFalse(is_perm("incest", "insects"))		

if __name__ == '__main__':
	unittest.main()