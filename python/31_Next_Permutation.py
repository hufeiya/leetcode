class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        founded = False
        for i in reversed(xrange(len(nums) -1)):
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while j > i:
                    if nums[j] > nums[i]:
                        nums[j],nums[i] = nums[i],nums[j]
                        break
                    j -= 1
                temp = nums[:i:-1]
                for t in xrange(len(temp)):
                    nums[i+t+1] = temp[t]
                founded = True
                break
        if not founded:
            nums.sort()
