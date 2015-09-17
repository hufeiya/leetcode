class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=2:
            return 0
        aList = [True] * (n)
        for i in xrange(2,n):
            if aList[i]:
                j = i + i
                for j in xrange(i+i,n,i):
                    aList[j] = False
        num = 0
        for i in xrange(2,n):
            if aList[i]:
                num += 1
        return num
