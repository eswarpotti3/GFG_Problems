from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        arr.sort()
        res = []

        # Step 2: answer each query using binary search
        for a, b in queries:
            # first index with value >= a
            left = bisect_left(arr, a)
            # first index with value > b
            right = bisect_right(arr, b)
            # elements in [a, b] are in arr[left:right]
            res.append(right - left)

        return res
        