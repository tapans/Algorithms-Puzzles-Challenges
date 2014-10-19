import sys

def max_rev_from_rod_cutting(prices, rod_size):
    ''' 
    Return [maximum revenue possible, size of first piece] by cutting rod of length rod_size into some finite number of pieces
    prices is an array of prices for various rod sizes where each index represents rod of size i + 1 inches
    '''
    
    max_revenues = range(rod_size+1)
    size_of_first_piece = range(rod_size+1)
    
    max_revenues[0] = 0
    for i in range(1, rod_size+1):
        max_rev_so_far = -sys.maxsize
        for j in range(1, i+1):
            cur_rev = prices[j-1] + max_revenues[i-j]
            if (cur_rev > max_rev_so_far):
                max_rev_so_far = cur_rev
                size_of_first_piece[i]=j
        max_revenues[i] = max_rev_so_far
    return [size_of_first_piece, max_revenues]

def print_optimal_solution_to_rod_cutting(prices, rod_size):
    '''    
    Print Max Revenue and list of piece sizes that solve the rod cutting problem for rod with length rod_length
    '''
    
    max_rev_and_first_piece_sizes = max_rev_from_rod_cutting(prices, rod_size)
    first_piece_sizes = max_rev_and_first_piece_sizes[0]
    max_revs = max_rev_and_first_piece_sizes[1]
        
    return [max_revs[rod_length], print_optimal_solution_to_rod_cutting_helper(first_piece_sizes, rod_length)]

def print_optimal_solution_to_rod_cutting_helper(first_piece_sizes, rod_length):
    '''
    Return a list of all the piece sizes in optimal solution of rod cutting such that sum of this list = rod_length
    '''
    
    if rod_length==0:
        return []
    else:
        return [first_piece_sizes[rod_length]] + print_optimal_solution_to_rod_cutting_helper(first_piece_sizes, rod_length - first_piece_sizes[rod_length])

if __name__ == '__main__':
    prices = [1,5,8,9,10,17,17,20,24,30]
    for rod_length in range(1, 11):
        print print_optimal_solution_to_rod_cutting(prices, rod_length)
        
    
    
    