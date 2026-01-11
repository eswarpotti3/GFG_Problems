class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        ans_start, ans_len = 0, float("inf")
        i = 0
        while i < n:
            if s1[i] == s2[0]:
                j = 0
                k = i
                while k < n and j < m:
                    if s1[k] == s2[j]:
                        j += 1
                    k += 1
                if j == m:
                    end = k - 1
                    j = m - 1
                    while end >= i:
                        if s1[end] == s2[j]:
                            j -= 1
                            if j < 0:
                                break
                        end -= 1
                    start = end
                    if ans_len > k - start:
                        ans_len = k - start
                        ans_start = start
                    i = start + 1
                else:
                    break
            else:
                i += 1
        if ans_len == float("inf"):
            return ""
        return s1[ans_start:ans_start + ans_len]
