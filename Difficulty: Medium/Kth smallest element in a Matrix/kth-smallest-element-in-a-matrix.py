import heapq

class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)
        heap = []

        for r in range(n):
            heapq.heappush(heap, (mat[r][0], r, 0))

        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (mat[r][c + 1], r, c + 1))

        return heap[0][0]
