from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):

        n = len(arr)
        left = 0
        freq = defaultdict(int)
        ans = 0

        for right in range(n):
            freq[arr[right]] += 1
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            ans += (right - left + 1)

        return ans
