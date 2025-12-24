class Solution:
    def countLessEqual(self, arr, x):
        arr.sort()
        #code here
        # arr.sort()
        # print(arr)
        #code here
        l=0
        r=len(arr)-1
        res=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]<=x:
                res=mid
                l=mid+1
            else:
                r=mid-1

        return  (res+1)