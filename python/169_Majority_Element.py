class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result,count = 0,0
        for i in nums:
            if count == 0:
                result = i
                count = 1
            elif result == i:
                count += 1
            else:
                count -= 1
        return result
