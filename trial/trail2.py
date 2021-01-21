def fun(xl1,xr1,yl1,yr1,xl2,xr2,yl2,yr2):
    # if x1==xr1 and x2==xr2 and y1==yr1 and y2==yr2:
    #     return 0
    
    # common=0
    # if x1<=xr1<=x2 and yr1==y2+1:
    #     common=x2-xr1+1

    # ht1=x2-x1+1
    # wdt1=y2-y1+1

    # area1=ht1*wdt1
    
    # ht2=xr2-xr1+1
    # wt2=yr2-yr1+1

    # area2=ht2*wt2

    # if area1==area2==common:
    #     return 0
    # area=area1+area2-common
    white1=0
    black1=0
    for i in range(xl1,xr1+1):
        for j in range(yl1,yr1+1):
            if i%2==1 and j%2==1:
                white1+=1
            elif i%2==1 and j%2==0:
                black1+=1
            elif i%2==0 and j%2==1:
                black1+=1
            else:
                white1+=1
    white2=0
    black2=0
    for i in range(xl2,xr2+1):
        for j in range(yl2,yr2+1):
            if i%2==1 and j%2==1:
                white2+=1
            elif i%2==1 and j%2==0:
                black2+=1
            elif i%2==0 and j%2==1:
                black2+=1
            else:
                white2+=1


    return white1*white2+black1*black2


print(fun(1,1,1,1,1,1,2,2))

