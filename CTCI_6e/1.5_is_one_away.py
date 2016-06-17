#!/usr/bin/python
import unittest

def is_one_away(s1, s2):
	'''
		Returns True if the two strings are one edit away. False o/w
			Edit could be an insertion/removal/replacement of a char
		Time Complexity: O(len(s1) + len(s2))
		Space Complexity: O(len(s1))

	'''

	s1_len = len(s1)
	s2_len = len(s2)
	if abs(s1_len - s2_len) > 1:
		return False
	else:
		char_counts = {}
		num_edits = 0
		for c in s1:
			if c in char_counts:
				char_counts[c] += 1
			else:
				char_counts[c] = 1
		for c in s2:
			if c not in char_counts:				
				num_edits += 1
				if num_edits > 1:
					return False
		return True

class Test_Is_Unique(unittest.TestCase):

	def test_one_away_case(self):
		self.assertTrue(is_one_away("mom", "mam"))
		self.assertTrue(is_one_away("mom", "moma"))
		self.assertTrue(is_one_away("mom", "om"))

	def test_not_one_away_case(self):
		self.assertFalse(is_one_away("mom", "tor"))
		self.assertFalse(is_one_away("mom", "mommy"))

if __name__ == '__main__':
	unittest.main()