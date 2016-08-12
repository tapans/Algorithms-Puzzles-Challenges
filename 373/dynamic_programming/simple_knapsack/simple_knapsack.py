def build_substructure(weights, k):
    ''' build a 2d array A where A[i,j]=1 if we can make total weight j using some subset of weights from w1,...,wi '''
    
    A = [[0 for i in range(len(weights)+1)] if j != 0 else [1 for i in range(len(weights)+1)] for j in range(k)]
    
    for i in range(1, k):
        for j in range(1, len(weights)+1):
            A[i][j] = A[i][j-1]
            if i-weights[j-1] >= 0:
                A[i][j]=max(A[i][j], A[i - weights[j-1]][j-1])
    return A

def simpleKnapsack(weights, k):
    ''' Return a subset S of weights such that weight(S) is max and weight(S) <= k '''
    
    A = [[[0, 0] for i in range(len(weights)+1)] if j != 0 else [[1, 0] for i in range(len(weights)+1)] for j in range(k+1)]
    
    for i in range(1, k+1):
        for j in range(1, len(weights)+1):
            if i-weights[j-1] >= 0 and A[i - weights[j-1]][j-1][0] > A[i][j-1][0]:
                A[i][j][0]=A[i - weights[j-1]][j-1][0]
                A[i][j][1]=(i - weights[j-1], j-1)
            elif A[i][j-1][0] > 0:
                A[i][j][0] = A[i][j-1][0]
                A[i][j][1] = (i, j-1)

                
    print A
    print A[5]
    #go thru A[5] in desc order, take first one with 1, and traverse

[[[1, 0], [1, 0], [1, 0], [1, 0], [1, 0]], [[0, 0], [0, (1, 0)], [1, (0, 1)], [1, (1, 2)], [1, (1, 3)]], [[0, 0], [0, (2, 0)], [0, (2, 1)], [1, (0, 2)], [1, (2, 3)]], [[0, 0], [1, (0, 0)], [1, (3, 1)], [1, (3, 2)], [1, (3, 3)]], [[0, 0], [0, (4, 0)], [1, (3, 1)], [1, (4, 2)], [1, (4, 3)]]]
    

if __name__=="__main__":
    weights = [3,1,2,1]
    k=5
    print simpleKnapsack(weights,k)
    
    