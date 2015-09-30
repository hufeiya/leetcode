class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        realPosition = 0
        for i in nums:
            if i != val:
                nums[realPosition] = i
                realPosition += 1
        return realPosition
