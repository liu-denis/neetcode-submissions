class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        for i in range(len(nums)):
            if nums[i] in nums[0:i] or nums[i] in nums[i+1:]:
                res = True 
                break
        return res