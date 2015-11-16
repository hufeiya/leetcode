class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right = 0,x
        while left <= right:
            mid = (left + right)/2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left-1
