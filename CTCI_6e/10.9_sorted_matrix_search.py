#!/usr/bin/python
import unittest

def sorted_matrix_search(M, e):
	'''
		Find element e in mxn Matrix M in which each row and column are sorted
		Return location (i,j) of element if found, -1 o/w
		Time Complexity: O(n+m)
		Space Complexity: O(1)
	'''

	num_rows = len(M)
	num_cols = len(M[0])
	if M[num_rows - 1][num_cols - 1] < e or M[0][0] > e:
		return -1

	row = 0
	col = num_cols - 1

	while row < num_rows and col >= 0:
		val = M[row][col]
		if val == e:
			return (row,col)
		elif e < val:
			col -= 1
		else:
			row += 1
	return -1

class Test_Sorted_Matrix_Search(unittest.TestCase):

	def test_basic(self):
		matrix = [[1,10,20,30],[4,15,25,35],[6,20,30,40],[8,25,35,43]]
		self.assertEquals(-1, sorted_matrix_search(matrix, 99))
		self.assertEquals((2,3), sorted_matrix_search(matrix,40))

if __name__ == '__main__':
	unittest.main()