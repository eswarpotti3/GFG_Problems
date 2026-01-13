class Solution:
    def canServe(self, arr):
        # code here 
        d={5:0,10:0,20:0}
        for i in arr:
            if i==5:
                d[5]+=1
            if i==10:
                # k=d[i]
                k=d[5]
                if k>0 :
                    d[5]-=1
                    d[10]+=1
                else:
                    return False
            if i==20:
                k=d[5]
                l=d[10]
                if k>0 and l>0:
                    d[5]-=1
                    d[10]-=1
                    d[20]+=1
                elif k>2:
                    d[5]-=3
                    d[20]+=1
                else:
                    return False
        return True