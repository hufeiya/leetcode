class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generate(n,'',0)
        return self.result
        
    def generate(self,n,string,lack):
        if n == 0:
            for i in range(lack):
                string += ')'
            self.result.append(string)
            return
        self.generate(n-1,string + '(',lack+1)
        if lack >0:self.generate(n,string + ')',lack-1)
