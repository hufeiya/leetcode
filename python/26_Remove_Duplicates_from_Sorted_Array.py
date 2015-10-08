class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        i,j,target = 0,1,nums[0]
        while i < len(nums):
            if nums[i] != target:
                target = nums[j] = nums[i]
                j += 1
            i += 1
        return j
