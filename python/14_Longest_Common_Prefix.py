class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0 or len(strs[0]) == 0:
            return ''
        str = ""
        for j in xrange(len(strs[0])):
            temp = strs[0][j]
            for i in strs[1:]:
                if len(i) <= j or i[j] != temp:
                    return str
            str += temp
        return str
                    
