class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m,n = n,m
        sum = [1]*m
        for i in xrange(1,n):
            for j in xrange(1,m):
                sum[j] += sum[j - 1]
        return sum[m - 1]
