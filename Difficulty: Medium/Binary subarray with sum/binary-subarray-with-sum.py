class Solution:
    def numberOfSubarrays(self, arr, k):
        def helper(x):
            if x<0:
                return 0
            curr=0
            i=0
            res=0
            for j in range(len(arr)):
                curr+=arr[j]
                while curr>x:
                    curr-=arr[i]
                    i+=1
                res+=(j-i+1)
                
            return res
                    
            
        return helper(k)-helper(k-1)