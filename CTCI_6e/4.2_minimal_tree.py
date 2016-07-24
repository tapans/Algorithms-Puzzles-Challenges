#!/usr/bin/python
import unittest
import logging
from binary_node import Binary_Node

def minimal_tree(sorted_arr):
	'''
		Return Binary Tree created from the sorted_arr with minimal height			
		Time Comlexity: O(n log n)
		Space Complexity: O(n)
	'''
	if len(sorted_arr) == 0:
		return None
	elif len(sorted_arr) == 1:
		return Binary_Node(sorted_arr[0], None, None)
	else:
		mid = len(sorted_arr) / 2
		return Binary_Node(sorted_arr[mid], minimal_tree(sorted_arr[:mid]), minimal_tree(sorted_arr[mid+1:]))

class Test_Minimal_Tree(unittest.TestCase):

	def test_minimal_tree(self):
		left_leaf = Binary_Node(6, None, None)
		second_left_leaf = Binary_Node(1, None, None)
		two_node = Binary_Node(2, second_left_leaf, None)
		seven_node = Binary_Node(7, left_leaf, None)
		correct_binary_tree = Binary_Node(4, two_node, seven_node)
		self.print_binary_tree(correct_binary_tree)
		print '--------'
		sorted_arr = [1,2,4,6,7]		
		result_tree = minimal_tree(sorted_arr)
		self.print_binary_tree(result_tree)
		print '--------'
		self.assertFalse(self.binary_tree_equals(correct_binary_tree, seven_node))
		self.assertTrue(self.binary_tree_equals(correct_binary_tree, correct_binary_tree))
		self.assertTrue(self.binary_tree_equals(result_tree, result_tree))

		print result_tree.num,result_tree.left.num, result_tree.right.num
		self.assertTrue(self.binary_tree_equals(correct_binary_tree, result_tree))
		

	def binary_tree_equals(self,a,b):
		
		if (a==None):
			return b==None
		elif (b==None):
			return False
		elif (a.num != b.num):
			return False
		else:
			return self.binary_tree_equals(a.left, b.left) and self.binary_tree_equals(a.right, b.right)

	def print_binary_tree(self, t):
		if t == None: return
		self.print_binary_tree(t.left)
		print t.num
		self.print_binary_tree(t.right)

if __name__ == '__main__':    
	unittest.main()