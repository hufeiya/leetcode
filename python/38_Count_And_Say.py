class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in xrange(n-1):
            t,temp,count = s[0],'',0
            for j in s:
                if j == t:
                    count += 1
                else:
                    temp += str(count) + t
                    count,t = 1,j
            s = temp + str(count) + t
        return s
