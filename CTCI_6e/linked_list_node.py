class Linked_List_Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next
		self.visited = False

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