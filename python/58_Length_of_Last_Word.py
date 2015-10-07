class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        s = s[::-1]
        start = False
        for i in s:
            if i != ' ':
                start = True
                length += 1
                continue
            if start:
                if i == ' ':
                    break
                else:
                    length += 1
        return length
