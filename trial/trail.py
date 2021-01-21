def findPaths(R, C, N, sr, sc):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nxt = [[0] * C for _ in range(R)]
        nxt[sr][sc] = 1

        ans = 0
        for time in range(N):
            print(time)
            cur = nxt
            nxt = [[0] * C for _ in range(R)]
            print(cur)
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    print('r c val',r,c,val)
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        print(nr,nc,val)
                        if 0 <= nr < R and 0 <= nc < C:
                            
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                            print('1:',nxt)
                        else:
                            ans += val
                            ans %= MOD
                            print('2:',ans)

        return ans



for len1 in range(1,5):
    for i in range(0,5-len1):
        j=i+len1
        print(i,j)

