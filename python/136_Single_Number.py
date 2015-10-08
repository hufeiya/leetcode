class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in xrange(1,len(nums)):
            result ^= nums[i]
        return result
