def fun(arr):
    mp = {0: 1}
    sm = 0
    count = 0
    for i in range(len(arr)):
        sm += arr[i]

        if sm in mp:

            count += mp[sm]
            mp[sm] += 1
        else:
            mp[sm] = 1
    return count
