class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        n1,n2 = len(first),len(last)
        for i in range(min(n1,n2)):
            if first[i]!=last[i]:
                return first[:i]
        return first[:min(len(first), len(last))]