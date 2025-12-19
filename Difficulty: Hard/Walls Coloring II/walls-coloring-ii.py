from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        # If only one color and more than one wall -> impossible
        if k == 1:
            return costs[0][0] if n == 1 else -1

        # dp for the previous row
        prev = [0] * k

        # Initialize for the first wall
        for c in range(k):
            prev[c] = costs[0][c]

        for i in range(1, n):
            # Find smallest and second smallest in prev
            min1 = float('inf')
            min2 = float('inf')
            idx1 = -1

            for c in range(k):
                val = prev[c]
                if val < min1:
                    min2 = min1
                    min1 = val
                    idx1 = c
                elif val < min2:
                    min2 = val

            curr = [0] * k
            for c in range(k):
                if c == idx1:
                    curr[c] = costs[i][c] + min2
                else:
                    curr[c] = costs[i][c] + min1

            prev = curr

        ans = min(prev)
        return ans if ans < float('inf') else -1
