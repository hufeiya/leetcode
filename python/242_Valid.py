class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
