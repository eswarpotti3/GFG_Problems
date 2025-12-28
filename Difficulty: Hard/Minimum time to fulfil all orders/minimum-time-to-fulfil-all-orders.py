import math

class Solution:
    def minTime(self, ranks, n):
        def donuts_in_time(t, r):
            D = 1 + 8 * t // r
            k = int((-1 + math.isqrt(D)) // 2)
            return k

        def can_make(t):
            total = 0
            for r in ranks:
                total += donuts_in_time(t, r)
                if total >= n:
                    return True
            return False

        lo = 0
        hi = max(ranks) * n * (n + 1) // 2
        ans = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
