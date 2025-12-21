
class Solution:
    def countXInRange(self, arr, queries):
        import bisect
        n = len(arr)
        ans = []

        for l, r, x in queries:
            # First and last occurrence of x in the whole array
            left = bisect.bisect_left(arr, x)      # first index >= x
            right = bisect.bisect_right(arr, x)    # first index > x

            # If x doesn't exist at all
            if left == right:
                ans.append(0)
                continue

            # Overlap of [left, right-1] with [l, r]
            start = max(left, l)
            end = min(right - 1, r)

            if start > end:
                ans.append(0)
            else:
                ans.append(end - start + 1)

        return ans
