#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node

def loop_detection(ll):
	'''
		Return True if linked list ll has a loop. False o/w		
		Time Complexity: O(n)
		Space Complexity: O(1)
	'''

	rabbit = ll
	tortoise = ll
	while rabbit.next is not None and rabbit.next.next is not None:		
		rabbit = rabbit.next.next
		tortoise = tortoise.next
		if rabbit == tortoise:
			return True
	return False
	

class Test_Remove_Dups(unittest.TestCase):	

	def test_loop_exists(self):
		tail = Linked_List_Node(5,None)
		three = Linked_List_Node(3, tail)
		four = Linked_List_Node(4, three)
		three_dup = Linked_List_Node(3, four)
		two = Linked_List_Node(2, three_dup)
		tail.next = three_dup
		ll = Linked_List_Node(1,two)
		
		self.assertEquals(True, loop_detection(ll))

	def test_loop_does_not_exist(self):
		three = Linked_List_Node(3, None)
		two = Linked_List_Node(2, three)		
		ll = Linked_List_Node(1,two)
		
		self.assertEquals(False, loop_detection(ll))

if __name__ == '__main__':    
	unittest.main()