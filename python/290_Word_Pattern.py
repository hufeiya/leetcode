class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlist = str.split()
        if len(pattern) != len(strlist):
            return False
        p2s = {}
        s2p ={}
        for i in xrange(len(pattern)):
            if pattern[i] not in p2s:
                if strlist[i] in s2p:
                    return False
                p2s[pattern[i]] = strlist[i]
                s2p[strlist[i]] = 1
            elif p2s[pattern[i]] != strlist[i]:
                return False
        return True
