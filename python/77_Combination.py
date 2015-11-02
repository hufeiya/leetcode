class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.getC(range(1,n+1),k)
        
            
    def getC(self,seq, k):
        if k == 0:
            return [[]]
        if len(seq) == k:
            return [list(seq)]
        res = []
        for i in range(0, len(seq)-k+1):
            temp = self.getC(seq[i+1:], k-1)
            for t in temp:
                res.append([seq[i]]+t)
        return res
        
    
