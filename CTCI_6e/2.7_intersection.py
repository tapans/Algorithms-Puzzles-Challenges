#!/usr/bin/python
import unittest
import logging
from linked_list_node import Linked_List_Node

def intersects(ll1, ll2):
	'''
		Return True if linked lists ll1 and ll2 intersect. False o/w
		let n be length of ll1, m be length of ll2
		Time Complexity: O(n+m)
		Space Complexity: O(1) using augmented linked list with visited boolean flag
	'''

	while ll1 is not None:
		ll1.visited = True
		ll1 = ll1.next
	
	while  ll2 is not None:
		if ll2.visited:
			return True
		ll2 = ll2.next
	return False
	

class Test_Intersects(unittest.TestCase):	

	def test_intersects(self):
		tail = Linked_List_Node(5,None)		
		three = Linked_List_Node(3, tail)
		four = Linked_List_Node(4, three)
		three_dup = Linked_List_Node(3, four)
		two = Linked_List_Node(2, three_dup)		
		ll_a = Linked_List_Node(1,two)


		ll_b = Linked_List_Node(5, two)
		self.assertEquals(True, intersects(ll_a, ll_b))

	def test_does_not_intersect(self):
		three = Linked_List_Node(3, None)
		two = Linked_List_Node(2, three)		
		ll_a = Linked_List_Node(1,two)

		three_b = Linked_List_Node(3, None)
		two_b = Linked_List_Node(2, three_b)		
		ll_b = Linked_List_Node(1,two_b)
		self.assertEquals(False, intersects(ll_a, ll_b))

if __name__ == '__main__':    
	unittest.main()