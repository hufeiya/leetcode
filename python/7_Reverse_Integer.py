class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegtive = False
        if x < 0:
            x = -x
            isNegtive = True
        s = str(x)
        x = int(s[::-1])
        if x > 2147483647 or x < -2147483648:
            return 0
        if isNegtive:
            return -x
        else:
            return x
