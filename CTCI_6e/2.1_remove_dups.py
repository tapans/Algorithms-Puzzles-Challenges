#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node

def remove_dups_in_ll(ll):
	'''
		Remove duplicates in an unsorted linked list
		Time Complexity: O(n)
		Space Complexity: O(n)
	'''

	seen = {}
	seen[ll.data] = 1
	root = ll
	while ll.next != None:		
		if (ll.next.data in seen):
			ll.next = ll.next.next			
		else:
			seen[ll.next.data] = 1
		ll = ll.next
	return root


class Test_Remove_Dups(unittest.TestCase):	

	def test_basic(self):
		tail = Linked_List_Node(5,None)		
		three = Linked_List_Node(3, tail)
		four = Linked_List_Node(4, three)
		three_dup = Linked_List_Node(3, four)
		two = Linked_List_Node(2, three_dup)		
		ll = Linked_List_Node(1,two)
		self.assertEquals(5,remove_dups_in_ll(ll).get_length())

if __name__ == '__main__':    
	unittest.main()