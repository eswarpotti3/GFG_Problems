class Solution:
    def maxSubarraySum(self, arr, k):
        maxsum=0

        for i in range(k):
            maxsum+=arr[i]
        # print(maxsum)
        sum=maxsum
        j=0
        for i in range(k,len(arr)):
            sum+=arr[i]
            sum-=arr[j] 
            j+=1
            # print(sum,maxsum,i)
            maxsum=max(sum,maxsum)
        return maxsum   