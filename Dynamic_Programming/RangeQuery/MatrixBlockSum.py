'''
1314. Matrix Block Sum
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

'''

def matrixBlockSum(mat, K):
    prefix=[[0 for i in range(len(mat[0])+1)] for _ in range(len(mat)+1)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            prefix[i+1][j+1]=mat[i][j]+prefix[i+1][j]+prefix[i][j+1]-prefix[i][j]
    
    answer=[[0 for i in range(len(mat[0])+1)] for _ in range(len(mat)+1)]

    for i in range(len(mat)+1):
        for j in range(len(mat[0])+1):
            r1,c1=max(0,i-K), max(0,j-K)
            r2,c2=min(len(mat)-1,i+K),min(len(mat[0])-1,j+K)
            answer[i][j]=prefix[r2+1][c2+1]-prefix[r2+1][c1]-prefix[r1][c2+1]+prefix[r1][c1]
    

    return answer