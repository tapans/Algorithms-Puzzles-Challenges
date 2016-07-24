#!/usr/bin/python
import unittest
import logging

class Binary_Node:
	def __init__(self, num, left, right):		
		self.num = num
		self.left = left
		self.right = right

	def print_bt(self):
		if self == None: return
		self.left.print_bt()
		print self.num
		self.right.print_bt()

class Singly_Linked_List_Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

	def get_length(self):
		length = 1		
		while self.next != None:
			self = self.next
			length += 1
		return length

	def print_ll(self):
		print self
		while self.next != None:
			self = self.next
			print self
		print '----'

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
				depths[depth] = Singly_Linked_List_Node(bt.num, None)
			else:
				ll = depths[depth]
				while ll is not None:
					prev = ll
					ll = ll.next
				prev.next = Singly_Linked_List_Node(bt.num, None)

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