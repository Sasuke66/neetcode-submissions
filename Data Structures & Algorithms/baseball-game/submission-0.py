class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for i in operations:
            if i=="+":
                result.append(result[-1]+result[-2])
            elif i=='C':
                result.pop()
            elif i=='D':
                a=result[-1]
                result.append(2*a)
            else:
                result.append(int(i))
        return sum(result)