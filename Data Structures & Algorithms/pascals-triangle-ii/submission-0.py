class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [0] * (rowIndex + 1)
        r[0] = 1
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                r[j] += r[j - 1]
        return r