class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.trace(k,n,[],range(1,10))
        return self.result
        
    def trace(self,k,n,element,avalible):
        if k == 0:
            if n == 0:
                self.result.append(element[:])
            return
        for i in xrange(len(avalible)):
            if len(element) and avalible[i] < element[-1]:
                continue
            temp = n - avalible[i]
            if temp < 0:return
            element.append(avalible[i])
            self.trace(k-1,temp,element,avalible[:i]+avalible[i+1:])
            element.pop()
            
