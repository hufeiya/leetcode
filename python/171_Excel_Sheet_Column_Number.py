class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        for i in s:
            if length:
                result += 26**(length - 1)*(ord(i) - 64) 
            length -= 1
        return result
