#!/usr/bin/python
import unittest

def is_unique(s):
	'''
		Returns True if string s has unique chars. False o/w
		Time Complexity: O(n)
		Space Complexity: O(n)
	'''
	seen = {}
	for c in s:
		if c in seen:
			return False
		else:
			seen[c] = c
	return True


class Test_Is_Unique(unittest.TestCase):

	def test_unique_case(self):
		self.assertTrue(is_unique("asdf"))

	def test_not_unique_case(self):
		self.assertFalse(is_unique("aaaa"))

if __name__ == '__main__':
	unittest.main()