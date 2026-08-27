class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        final = nums[0]
        for i in nums[1:]:
            final = max(i, final + i)
            curr = max(curr, final)
        return curr