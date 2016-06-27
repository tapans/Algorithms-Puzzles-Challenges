#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node

def delete_middle_node(ll_middle):
	'''
		Delete node ll_middle from linked list. nothing is returned		
	'''

	if not ll_middle or ll_middle.next is None:
		return -1

	ll_middle.data = ll_middle.next.data
	ll_middle.next = ll_middle.next.next
	

class Test_Delete_Middle_Node(unittest.TestCase):	

	def test_basic(self):
		tail = Linked_List_Node(5,None)		
		three = Linked_List_Node(3, tail)
		four = Linked_List_Node(4, three)
		three_dup = Linked_List_Node(3, four)
		two = Linked_List_Node(2, three_dup)		
		ll = Linked_List_Node(1,two)
		delete_middle_node(three_dup)
		self.assertEquals(5,ll.get_length())

if __name__ == '__main__':    
	unittest.main()