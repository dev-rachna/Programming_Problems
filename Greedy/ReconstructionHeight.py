'''
406. Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

def reconstructQueue(people):
    people.sort()
    ans=[[[-1]*2] for i in range(len(people))]
    count=0
    for i in range(len(people)):
        count=people[i][1]

        for j in range(len(people)):
            if ans[j][0]==-1 and count==0:
                ans[j][0]=people[j][0]
                ans[j][1]=people[j][1]
                break
            elif ans[j][0]==-1 or ans[j][0]>=people[i][0]:
                count-=1
    
    return ans

