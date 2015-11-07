class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.temp = []
        self.result = []
        nums.sort()
        self.trace(0,nums)
        return self.result
        
    def trace(self,i,nums):
        if i == len(nums):
            self.result.append(self.temp[:])
            return
        self.temp.append(nums[i])
        self.trace(i+1,nums)
        self.temp.pop()
        self.trace(i+1,nums)
