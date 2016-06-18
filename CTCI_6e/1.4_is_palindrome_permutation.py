#!/usr/bin/python
import unittest

def is_palindrome_permutation(s):
	'''
		Returns True if string s is a permutation of a palindrome, False o/w
		Time Complexity: O(n)
		Space Complexity: O(n)
	'''

	s = s.lower().replace(" ", "")
	char_counts = {}	
	for c in s:
		if c in char_counts:
			if char_counts[c] > 1:
				return False
			char_counts[c] += 1
		else:
			char_counts[c] = 1

	num_single_counts = 0
	for c in char_counts:
		if char_counts[c] == 1:
			num_single_counts += 1
			if num_single_counts > 1:
				return False
		
	return True


class Test_Is_Palindrom_Permutation(unittest.TestCase):

	def test_palindrome_permutation_case(self):
		self.assertTrue(is_palindrome_permutation("Tact Coa"))

	def test_not_palindrome_permutation_case(self):
		self.assertFalse(is_palindrome_permutation("aficionado"))

if __name__ == '__main__':
	unittest.main()