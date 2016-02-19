class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)

#通过观察试验发现只有能被4整除的情况下nim才会赢
