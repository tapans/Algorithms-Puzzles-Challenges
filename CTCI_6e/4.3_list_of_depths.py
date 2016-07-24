#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node
from binary_node import Binary_Node

def list_of_depths(binary_tree):
	'''
		Return linked lists of all the nodes at each depth
		Time Comlexity: O(n)
		Space Complexity: O(n)
	'''
	depths = {}
	def pre_ord_traverse_bt(bt, depth=0):
		if bt is not None:			
			if depth not in depths:
				depths[depth] = Linked_List_Node(bt.num, None)
			else:
				ll = depths[depth]
				while ll is not None:
					prev = ll
					ll = ll.next
				prev.next = Linked_List_Node(bt.num, None)

			pre_ord_traverse_bt(bt.left, depth + 1)
			pre_ord_traverse_bt(bt.right, depth + 1)
	
	pre_ord_traverse_bt(binary_tree)
	return depths


class Test_List_of_depths(unittest.TestCase):

	def test_list_of_depths(self):
		left_leaf = Binary_Node(6, None, None)
		second_left_leaf = Binary_Node(1, None, None)
		two_node = Binary_Node(2, second_left_leaf, None)
		seven_node = Binary_Node(7, left_leaf, None)
		correct_binary_tree = Binary_Node(4, two_node, seven_node)
		depths = list_of_depths(correct_binary_tree)
		map(lambda ll: ll.print_ll(), depths.values())
		
if __name__ == '__main__':    
	unittest.main()