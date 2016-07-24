#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node

def kth_to_last(ll, k):
	'''
		Return kth to last node from Linked List ll
		Time Complexity: O(n)
		Space Complexity: O(1)
	'''

	i = 0
	ahead_ptr = ll
	while i < k:
		if not ahead_ptr.next:
			return -1
		else:
			ahead_ptr = ahead_ptr.next
			i += 1
	while ahead_ptr.next is not None:
		ahead_ptr = ahead_ptr.next
		ll = ll.next
	return ll


class Test_Kth_To_Last(unittest.TestCase):	

	def test_basic(self):
		tail = Linked_List_Node(5,None)		
		three = Linked_List_Node(3, tail)
		four = Linked_List_Node(4, three)
		three_dup = Linked_List_Node(3, four)
		two = Linked_List_Node(2, three_dup)		
		ll = Linked_List_Node(1,two)
		self.assertEquals(2,kth_to_last(ll, 4).data)

if __name__ == '__main__':    
	unittest.main()