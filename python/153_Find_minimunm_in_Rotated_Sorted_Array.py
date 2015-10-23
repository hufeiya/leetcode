class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right,minval = 0,len(nums)-1,nums[0]
        while left < right - 1:
            mid = (left + right)/2
            if nums[left] < nums[mid]:
                minval = min(nums[left],minval)
                left = mid + 1
            else:
                minval = min(nums[mid],minval)
                right = mid - 1
        minval = min(nums[left],nums[right],minval)
        return minval
