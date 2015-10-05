import Queue
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroItr = -1
        for i in xrange(len(nums)):
            if nums[i] == 0 and zeroItr == -1:
                zeroItr = i
            elif nums[i] != 0 and zeroItr != -1:
                nums[zeroItr],nums[i] = nums[i],0
                zeroItr += 1
