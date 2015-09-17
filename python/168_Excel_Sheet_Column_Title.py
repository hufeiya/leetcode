class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result  = ""
        while n > 0:
            result += chr((n-1) % 26 + 65)
            n = (n-1) / 26
        return result[::-1]
        
