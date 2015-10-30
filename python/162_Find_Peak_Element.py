class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,float("-inf"))
        nums.append(float("-inf"))
        left,right = 1,len(nums)-2
        while left <= right:
            mid = (left + right)/2
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid - 1
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
