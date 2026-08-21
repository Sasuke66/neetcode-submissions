class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, n = 0, len(t)
        for a in s:
            if i < n and t[i] == a:
                i += 1
        return n - i