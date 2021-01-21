'''
leetcode 1020. Number of Enclaves
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.
'''


def dfs(i, j, A):

    if i < 0 or i >= len(A) or j >= len(A[0]) or j < 0 or A[i][j] != 1:
        return

    A[i][j] = 2
    dfs(i+1, j, A)
    dfs(i-1, j, A)
    dfs(i, j+1, A)
    dfs(i, j-1, A)


def numEnclaves(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """

    for i in range(len(A)):
        if A[i][0] == 1:
            dfs(i, 0, A)
        if A[i][-1] == 1:
            dfs(i, len(A[0])-1, A)

    for j in range(len(A[0])):
        if A[0][j] == 1:
            dfs(0, j, A)
        if A[-1][j]:
            dfs(len(A)-1, j, A)

    count = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 1:
                count += 1

    return count


print(numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
