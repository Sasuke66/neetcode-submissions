class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                backtrack(i, target - nums[i], path + [nums[i]])
        result = []
        nums.sort()
        backtrack(0, target, [])
        return result