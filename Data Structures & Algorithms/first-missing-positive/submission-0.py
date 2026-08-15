class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()
        value = 1
        for n in nums:
            if n == value:
                value += 1
            elif n > value:
                return value
        return value