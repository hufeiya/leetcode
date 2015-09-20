class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        nums.sort()
        result = [nums[:]]
        flag = True
        while flag:
            for i in reversed(xrange(len(nums) - 1)):
                if nums[i] < nums[i + 1]:
                    t = len(nums) - 1
                    while t > i:
                        if nums[t] > nums[i]:
                            nums[i],nums[t] = nums[t],nums[i]
                            break
                        t -= 1
                    temp = nums[:i:-1]
                    for j in xrange(len(temp)):
                        nums[i+j+1] = temp[j]
                    result.append(nums[:])
                    break
                elif i == 0:
                    flag = False
        return result
            
