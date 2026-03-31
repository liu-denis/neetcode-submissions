class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        count_lst = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count_lst.append(count)
                count = 0
        return max(count_lst)

