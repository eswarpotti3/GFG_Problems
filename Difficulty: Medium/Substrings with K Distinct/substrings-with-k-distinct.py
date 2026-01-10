class Solution:
    def countSubstr (self, s, k):
        def at_most(k):
            if k < 0:
                return 0
            freq = {}
            left = 0
            res = 0
            distinct = 0

            for right, ch in enumerate(s):
                if ch not in freq or freq[ch] == 0:
                    distinct += 1
                freq[ch] = freq.get(ch, 0) + 1
                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1
                res += (right - left + 1)

            return res

        return at_most(k) - at_most(k - 1)
