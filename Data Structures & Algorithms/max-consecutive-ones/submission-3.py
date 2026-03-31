class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        old, new = 0, 0

        for num in nums:
            if num == 1:
                new += 1
            else:
                old = max(old, new)
                new = 0

        return max(old, new)
        

