class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        sumList = [0]*len(nums)
        sumList[0] = nums[0]
        for i in xrange(1,len(nums)):
            sumList[i] = max(sumList[i-1] , sumList[i-2] + nums[i])
        return sumList[-1]
            
