class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        def helper(x):
            if x<0:return 0
            s=0
            l,j=0,0
            res=0
            for j in range(len(arr)):
                s+=arr[j]%2
                while s>x:
                    s-=arr[l]%2
                    l+=1
                res+=(j-l+1)
                
            return res
                    
            
        return helper(k)-helper(k-1)