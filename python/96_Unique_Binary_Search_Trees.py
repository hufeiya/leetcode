class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1,1,2]
        for i in xrange(3,n+1):
            temp = 0
            for j in xrange(1,i+1):
                temp += nums[j-1]*nums[i-j]
            nums.append(temp)
        return nums[n]
