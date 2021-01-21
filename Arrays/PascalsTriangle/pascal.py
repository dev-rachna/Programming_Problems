def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        
        triangle=[]
        triangle.append([1])
        
        for i in range(1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(triangle[-1][j-1]+triangle[-1][j])
            row.append(1)
            triangle.append(list(row))

        print(triangle)

generate(4)