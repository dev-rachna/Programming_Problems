#IB 


def fun(points):
    seen=set()
    count=0
    maxi=0
    for i in range(len(points)):
        x1,y1=points[i] #fix 1st pt
        for x2,y2 in seen: #loop for 2nd diagonal pt
            if (x2,y1) in seen and (x1,y2) in seen:
                count+=1
                maxi=max(maxi,abs(x2-x1)*abs(y2-y1))
        seen.add((x1,y1))
    #return maxi
    return count


