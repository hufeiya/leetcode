class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length,sublen = len(haystack),len(needle)
        for i in xrange(length - sublen + 1):
            if haystack[i:i+sublen] == needle:
                return i
        return -1
