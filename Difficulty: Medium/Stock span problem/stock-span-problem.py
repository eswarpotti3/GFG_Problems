class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        st = []
        for i in range(n):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            span[i] = i + 1 if not st else i - st[-1]
            st.append(i)
        return span
