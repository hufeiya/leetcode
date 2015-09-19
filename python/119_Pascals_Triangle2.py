class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(1,rowIndex + 1):
            result = [1] + [result[j-1] + result[j] for j in range(1,i)] + [1]
        return result
