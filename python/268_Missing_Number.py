class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1,len(nums)+1):
            result ^= i
        for i in range(0,len(nums)):
            result ^= nums[i]
        return result
