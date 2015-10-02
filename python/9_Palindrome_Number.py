class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        big = 1
        while x / big >= 10:
            big *= 10
        while 10 <= big:
            if x / big != x % 10:
                return False
            x /= 10
            big /= 10
            x %= big
            big /= 10
        return True
