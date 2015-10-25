class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero,two,itr = 0,len(nums)-1,0
        while itr <= two:
            if nums[itr] == 0:
                nums[itr],nums[zero] = nums[zero],nums[itr]
                zero += 1
            elif nums[itr] == 2:
                nums[itr],nums[two] = nums[two],nums[itr]
                two -= 1
                itr -= 1
            itr += 1
