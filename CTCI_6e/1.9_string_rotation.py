#!/usr/bin/python
import unittest

def isSubstring(s1, s2):
	'''
		Returns True if s2 is a substring of s1
	'''
	return s1 in s2

def is_string_rotation(s1,s2):
	''' 
		Returns True if s2 is a rotation of s1 using only one call to isSubstring. False o/w
		Time Complexity: let a be len of s1, b be len of s2, and let  b > a => O(b log b)
		Space Complexity: O(1)
	'''

	s1_sorted = ''.join(sorted(s1))
	s2_sorted = ''.join(sorted(s2))
	return isSubstring(s1_sorted, s2_sorted)		


class Test_String_Rotation(unittest.TestCase):

	def test_is_substring_case(self):
		self.assertTrue(is_string_rotation("waterbottle", "erbottlewat"))

	def test_not_substring_case(self):
		self.assertFalse(is_string_rotation("hi", "bye"))

if __name__ == '__main__':
	unittest.main()