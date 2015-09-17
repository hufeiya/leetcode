class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.__rotate(nums,0,len(nums))
        self.__rotate(nums,0,k)
        self.__rotate(nums,k,len(nums))
        
    def __rotate(self,nums,start,end):
        while start < end:
            nums[start],nums[end-1] = nums[end-1],nums[start]
            start += 1
            end -= 1
            
