class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in xrange(n):
            temp = 1 << i
            for i in xrange(len(result)-1,-1,-1):
                result.append(temp + result[i])
        return result
