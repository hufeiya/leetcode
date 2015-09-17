class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split('.')
        s2 = version2.split('.')
        length = max(len(s1),len(s2))
        for i in xrange(length):
            if i >= len(s1):
                if int(s2[i]) == 0:
                    continue
                else :
                    return -1
            elif i >= len(s2):
                if int(s1[i]) == 0:
                    continue
                else:
                    return 1
            elif int(s1[i]) < int(s2[i]):
                return -1
            elif int(s1[i]) > int(s2[i]):
                return 1
            else :
                continue
        return 0
