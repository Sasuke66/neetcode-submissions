class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            prev_max = 0
            curr_max = 0
            for x in nums:
                temp = max(curr_max, prev_max + x)
                prev_max = curr_max
                curr_max = temp
            return curr_max
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])