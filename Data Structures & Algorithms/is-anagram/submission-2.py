class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for c in s:
            if c not in count_s:
                count_s[c] = 0
            count_s[c] += 1

        for c in t:
            if c not in count_t:
                count_t[c] = 0
            count_t[c] += 1 

        return count_t == count_s    