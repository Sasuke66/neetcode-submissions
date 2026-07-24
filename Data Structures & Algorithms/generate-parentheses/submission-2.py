class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        ans = []
        def backtrack(opens, closes):
            if opens == closes == n:
                ans.append(''.join(sol))
                return
            if opens < n:
                sol.append('(')
                backtrack(opens + 1, closes)
                sol.pop()
            if closes < opens:
                sol.append(')')
                backtrack(opens, closes + 1)
                sol.pop()
        backtrack(0, 0)
        return ans