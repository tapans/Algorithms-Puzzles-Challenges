#!/usr/bin/python
import unittest

def urlify(s):
	''' 
		Returns string s with all spaces replaced with %20
		Time Complexity: O(n)
		Space Complexity: O(n)
		Note: if instead we had a pointer to the string in C, 
			we could have O(1) space by computing new length of string, 
			and then overwriting the chars in reverse in memory
	'''

	s_arr = list(s)
	for i in range(len(s_arr)):
		if s_arr[i] == ' ':
			s_arr[i] = '%20'
	return ''.join(s_arr)


class Test_Urlify(unittest.TestCase):

	def test_urlify(self):
		self.assertEquals(urlify("a b d"), 'a%20b%20d')
		self.assertEquals(urlify("Bond. James Bond"), 'Bond.%20James%20Bond')

if __name__ == '__main__':
	unittest.main()