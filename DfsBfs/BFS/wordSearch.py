# -*- coding: utf-8 -*-


def bfs(i,j,board,word,l):
    if len(word)==l:
        return True
    
    if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or board[i][j]!=word[l]:
        return False
    
    temp=board[i][j]
    board[i][j]='*'
    
    print(board,word[l],i,j,l)
    # for ni,nj in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
    #             if bfs(ni,nj,board,word,l+1):
    #                 return True
    
    if bfs(i+1,j,board,word,l+1) or bfs(i-1,j,board,word,l+1) or bfs(i,j+1,board,word,l+1) or bfs(i,j-1,board,word,l+1):
        return True
    board[i][j]=temp
    return False
    


def wordSearch(board,word):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0]:
                if bfs(i,j,board,word,0):
                    return True
    return False


res=wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")           
print(res)
