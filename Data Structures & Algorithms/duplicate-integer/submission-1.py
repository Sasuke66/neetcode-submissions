class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        nums2 = list(set(nums))
        return len(nums) != len(nums2)

        