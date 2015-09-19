class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1,1])
        for i in xrange(2,numRows):
            temp = [1] * (i + 1) 
            pre = result[i-1]
            for j in xrange(1,(i + 1)/2 + 1):
                temp[j] = pre[j-1] + pre[j]
            for j in xrange((i + 1)/2,i):
                temp[j] = temp[i-j]
            result.append(temp)
        return result
