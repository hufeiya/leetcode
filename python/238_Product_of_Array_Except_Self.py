class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        i = len(nums) - 1
        while i > 0:
            result[i-1] = result[i]*nums[i]
            i -= 1
        left = 1
        for i in xrange(len(nums)):
            result[i] *= left
            left *= nums[i]
        return result
