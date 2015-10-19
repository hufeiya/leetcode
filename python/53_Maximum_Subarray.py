class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsum = result = nums[0]
        for i in xrange(1,len(nums)):
            if subsum < 0:subsum = 0
            subsum += nums[i]
            result = max(result,subsum)
        return result
