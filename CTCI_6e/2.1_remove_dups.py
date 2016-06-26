#!/usr/bin/python
import unittest
import logging

class Linked_List_Node:
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

def remove_dups_in_ll(ll):
	'''
		Remove duplicates in an unsorted linked list 
	'''

	seen = []
	seen.append(ll.data)
	root = ll
	while ll.next != None:		
		if (ll.next.data in seen):
			ll.next = ll.next.next			
		else:
			seen.append(ll.next.data)
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