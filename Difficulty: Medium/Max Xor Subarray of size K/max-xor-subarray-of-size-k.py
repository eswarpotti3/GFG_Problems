class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # Build prefix XOR array
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        
        ans = 0
        # First window [0 .. k-1]
        ans = prefix[k - 1]
        
        # Slide windows ending at end = k-1 .. n-1
        for end in range(k - 1, n):
            start = end - k + 1
            if start == 0:
                curr = prefix[end]
            else:
                curr = prefix[end] ^ prefix[start - 1]
            if curr > ans:
                ans = curr
        
        return ans
