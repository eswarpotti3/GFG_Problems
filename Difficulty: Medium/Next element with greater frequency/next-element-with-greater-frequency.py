from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)         
        res = [-1] * n
        st = []                     
        for i in range(n - 1, -1, -1):
            while st and freq[arr[st[-1]]] <= freq[arr[i]]:
                st.pop()

            if st:
                res[i] = arr[st[-1]]
            else:
                res[i] = -1

            st.append(i)

        return res
