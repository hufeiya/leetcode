class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        if not nums:
            return result
        start,end = nums[0],nums[0]
        length = len(nums)
        for i in xrange(1,length + 1):
            if i < length and nums[i] - end == 1:
                end = nums[i]
            else:
                if start >= end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                if i < length:
                    start = end = nums[i]
        return result
            
