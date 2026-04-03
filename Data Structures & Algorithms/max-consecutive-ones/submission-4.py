class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        
        for n in nums:
            if n == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        return max(max_count, count)