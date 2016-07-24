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
