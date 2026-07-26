class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        result = []
        for x in hashmap:
            if hashmap[x] == 1:
                result.append(x)
        return result