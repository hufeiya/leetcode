class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            sum += n/5
            n /= 5
        return sum
