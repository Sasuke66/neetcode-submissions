class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in hm:
                if abs(hm[nums[i]] - i) <= k:
                    return True
            hm[nums[i]] = i
        return False