#!/usr/bin/python
import unittest

def simple_string_compress(s):
	''' 
		Replace consecutive instance of same alphabet with a number
		ex: aaaaabbccc becomes a5b2c3
		Time Complexity: O(n)
		Space Complexity: O(n)
	'''

	old_len = len(s)
	if old_len <= _count_compression(s):
		return s
	prev = s[0]
	curr_count = 1
	new_s = ""	
	for i in range(1, old_len):
		if s[i] == prev:
			curr_count += 1			
		else:
			new_s += prev + str(curr_count)
			prev = s[i]
			curr_count = 1
	new_s += prev + str(curr_count)	
	return new_s 

def _count_compression(s):
	compressed_len = 0	
	s_len = len(s)
	for i in range(s_len):		
		if (i+1 >= s_len or s[i] != s[i+1]):
			compressed_len += 2		
	return compressed_len


class Test_Simple_String_Compress(unittest.TestCase):

	def test_simple_string_compress(self):
		self.assertEquals(simple_string_compress("aaaaabbccc"), "a5b2c3")
		self.assertEquals(simple_string_compress("abcd"), "abcd")

if __name__ == '__main__':
	unittest.main()