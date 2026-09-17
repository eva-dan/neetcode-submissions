class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = 26*[0]
        for i in range(len(s)):
            idx_s = ord(s[i]) - ord("a")
            count[idx_s] += 1
            idx_t = ord(t[i]) - ord("a")
            count[idx_t] -= 1
        return all(c == 0 for c in count)