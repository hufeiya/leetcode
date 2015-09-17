class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashTable = {}
        h2 = {}
        for i in xrange(len(s)):
            if s[i] not in hashTable:
                if t[i] in h2:
                    return False
                hashTable[s[i]] = t[i]
                h2[t[i]] = s[i]
            else:
                if hashTable[s[i]] != t[i]:
                    return False
        return True
