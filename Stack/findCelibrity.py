'''
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.

We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem.
Examples:

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2
Explanation: The person with ID 2 does not 
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity
'''

def fun(matrix):
    stack=[i for i in range(len(matrix))]
    while len(stack)!=1:
        first=stack.pop()
        second=stack.pop()

        if matrix[first][second]==1:
            stack.append(second)
        elif matrix[first][second]==0:
            stack.append(first)
    
    celebrity=stack.pop()
    print(celebrity)

    for i in range(len(matrix)):
        if i==celebrity and matrix[celebrity][i]==0 :
            continue
        elif matrix[celebrity][i]!=0 and matrix[i][celebrity]!=1:
            print('false')
            break
        else:
            print('false1')
            return
    print('here')
    



fun([[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]])