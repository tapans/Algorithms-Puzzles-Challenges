#!/usr/bin/python
import unittest

def zero_matrix(m):
	''' 
		Replace rows and columns of Matrix mxn with 0 if an element of the matrix is 0
		Time Complexity: O(mxn)
		Space Complexity: O(1)
	'''

	num_rows = len(m)
	for r in range(num_rows):
		num_cols = len(m[r])
		for c in range(num_cols):
			if m[r][c] == 0:
				if r == 0 and c == 0:
					m[0][0] = 'zero'
				elif r == 0:
					m[r][0]='zero'
					m[0][c]='zero'
					m[0][0] = 'row'
				elif c == 0:
					m[r][0]='zero'
					m[0][c]='zero'
					m[0][0] = 'col'
				else:
					m[r][0]='zero'
					m[0][c]='zero'


	for r in range(num_rows):
		num_cols = len(m[r])
		for c in range(num_cols):
			if ((m[r][0] == 'zero' or m[0][c] == 'zero') and m[r][c] != 'zero'):
				m[r][c] = 0
			elif (m[0][0] == 'row' and r == 0 and m[r][c] != 'row' and m[r][c] != 'zero'):
				m[r][c] = 0
			elif (m[0][0] == 'col' and c == 0 and m[r][c] != 'col' and m[r][c] != 'zero'):
				m[r][c] = 0

	for r in range(num_rows):
		num_cols = len(m[r])
		for c in range(num_cols):
			if m[r][c] == 'zero':
				m[r][c] = 0
			elif m[r][c] == 'col':
				m[r][c] = 0
			elif m[r][c] == 'row':
				m[r][c] = 0

	return m			


class Test_Zero_Matrix(unittest.TestCase):

	def test_zero_matrix(self):
		self.assertEquals([[1,2,3,0],[0,0,0,0]], zero_matrix([[1,2,3,4],[5,2,6,0]]))
		self.assertEquals([[0,2,3],[0,5,6],[0,0,0]], zero_matrix([[1,2,3],[4,5,6],[0,8,9]]))

if __name__ == '__main__':
	unittest.main()