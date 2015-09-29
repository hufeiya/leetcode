class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return n
        pre,next = 1,2
        for i in xrange(2,n):
            pre,next = next,pre + next
        return next
