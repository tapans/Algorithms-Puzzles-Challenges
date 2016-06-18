#!/usr/bin/python
import unittest

# def print_nxn_mat(m):
# 	s=[[str(c) for c in row] for row in m]
# 	lens = [max(map(len,col)) for col in zip(*s)]
# 	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
# 	table = [fmt.format(*row) for row in s]
# 	print '\n'.join(table)

def rotate_matrix(m):
	'''
		Rotate matrix m of size nxn by 90 degrees clockwise
		Time Complexity: O(nxn)
		Space Complexity: O(nxn)
	'''

	n = len(m[0])
	new_m = [[0 for j in range(n)] for j in range(n)]
	
	for r in range(n):		
		for c in range(n):
			new_m[r][c] = m[n - 1 - c][r]	
	return new_m

def rotate_matrix_in_place(m):
	'''
		Rotate matrix m of size nxn by 90 degrees clockwise
		Time Complexity: O(nxn)
		Space Complexity: O(1)
	'''

	n = len(m[0])
	num_layers = n / 2
	
	layer_start_index = 0
	layer_end_index = n - 1
	for l in range(num_layers):
		for k in range(layer_start_index, layer_end_index):
			#top row cells go to right cols
			right_col_val = m[k][layer_end_index]
			m[k][layer_end_index] = m[layer_start_index][k]

			#right col cells go to bottom row
			bottom_row_val = m[layer_end_index][n - 1 - k]
			m[layer_end_index][n - 1 - k] = right_col_val

			#bottom col cells go to left col
			left_col_val = m[n - 1 - k][layer_start_index]
			m[n - 1 - k][layer_start_index] = bottom_row_val

			#left col cells go to top row
			m[layer_start_index][k] = left_col_val
		layer_start_index += 1
		layer_end_index -= 1
	#print print_nxn_mat(m)
	return m

class Test_Rotate_Matrix(unittest.TestCase):

	def test_regular_case(self):
		self.assertEquals([[0,1],[1,0]], rotate_matrix([[1,0],[0,1]]))
		self.assertEquals([[7,4,1],[8,5,2],[9,6,3]], rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
		self.assertEquals([[31,25,19,13,7,1],[32,26,20,14,8,2],[33,27,21,15,9,3],[34,28,22,16,10,4],[35,29,23,17,11,5],[36,30,24,18,12,6]], rotate_matrix([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]))

	def test_in_place_case(self):
		self.assertEquals([[0,1],[1,0]], rotate_matrix_in_place([[1,0],[0,1]]))
		self.assertEquals([[7,4,1],[8,5,2],[9,6,3]], rotate_matrix_in_place([[1,2,3],[4,5,6],[7,8,9]]))
		self.assertEquals([[31,25,19,13,7,1],[32,26,20,14,8,2],[33,27,21,15,9,3],[34,28,22,16,10,4],[35,29,23,17,11,5],[36,30,24,18,12,6]], rotate_matrix_in_place([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]))


if __name__ == '__main__':
	unittest.main()