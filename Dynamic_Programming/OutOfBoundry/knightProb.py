'''
576. Out of Boundary Paths

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

'''
def fun(R, C, N, sr, sc):
    next=[[0 for i in range(C)] for _ in range(R)]
    next[sr][sc]=1
    MOD = 10**9 + 7

    for i in range(N):
        curr=[[0 for i in range(C)] for _ in range(R)]
        for row_index,entire_row in enumerate(next):
            for col_index,value in enumerate(entire_row):
                for mov_row,mov_col in[(1,0),(-1,0),(0,1),(0,-1)]:

                    if 0<=mov_row+row_index<R and 0<=mov_col+col_index<C:
                        curr[mov_row+row_index][mov_col+col_index]+=value
                        curr[mov_row+row_index][mov_col+col_index]%=MOD
                    else:
                        ans+=value
                        ans%=MOD
        

        next=curr
