class Solution:
    def findPeakGrid(self, mat):
        m=len(mat)
        n=len(mat[0])
        
        for i in range(m):
            flag=False
            upper=-99999999
            down=-9999999
            left=-9999999
            right=-99999999
            for j in range(n):
                x=mat[i][j]
                # print(x,i,j)
                # print("--------------")
                if i>0:
                    upper=mat[i-1][j]
                
                if j>0:
                    left=mat[i][j-1]
                if j<n-1:
                    right=mat[i][j+1]
        
                if i<m-1:
                    down=mat[i+1][j]
                # print(upper,down,left,right)
                if (x>=upper)and (x>=down) and (x>=left) and (x>=right):
                    # flag=True
                    return (i,j)
                # print("----------------")
                  
            # if flag:break
                
        return False
                