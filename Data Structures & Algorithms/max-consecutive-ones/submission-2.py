class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a, b = 0, 0

        for num in nums:
            if num == 1:
                b += 1
            else:
                a = max(a, b)
                b = 0
        return max(a, b)
        

