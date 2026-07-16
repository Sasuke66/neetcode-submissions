class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        l = -1
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = l
            l = max(l, curr)
        return arr
            