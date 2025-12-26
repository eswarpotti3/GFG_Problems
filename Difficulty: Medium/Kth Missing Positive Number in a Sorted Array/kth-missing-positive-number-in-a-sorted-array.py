class Solution:
    def kthMissing(self, arr, k):
        
        missing = 0
        curr = 1
        i = 0
        n = len(arr)

        while True:
            if i < n and arr[i] == curr:
                i += 1
            else:
                missing += 1
                if missing == k:
                    return curr
            curr += 1
