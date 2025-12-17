class Solution:
    def mergeOverlap(self, arr):
        # arr is a list of [start, end]
        if not arr:
            return []

        # 1. Sort intervals by start time
        arr.sort(key=lambda x: x[0])

        merged = []
        for interval in arr:
            if not merged or merged[-1][1] < interval[0]:
                # No overlap, add interval
                merged.append(interval)
            else:
                # Overlap: merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
