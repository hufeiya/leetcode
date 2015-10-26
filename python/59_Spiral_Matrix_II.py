class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [([0]*n)for i in range(n)]
        i,left,right,top,bottom = 1,0,n-1,0,n-1
        while i < n * n:
            for j in xrange(left,right):
                m[top][j] = i
                i += 1
            for j in xrange(top,bottom):
                m[j][right] = i
                i += 1
            for j in xrange(right,left,-1):
                m[bottom][j] = i
                i += 1
            for j in xrange(bottom,top,-1):
                m[j][left] = i
                i += 1
            left,right,top,bottom = left + 1,right - 1,top + 1,bottom - 1
        if n%2:m[n/2][n/2] = n*n
        return m
