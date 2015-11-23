class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.num = num
        self.size = len(num)
        self.result = False
        for i in xrange(1,self.size/2+1):
            self.order(self.sumLength(0,i),i)
        return self.result
        
    def sumLength(self,start,end):
        if end <= self.size and (self.num[start] != '0' or end - start == 1):
            return int(self.num[start:end])
        return -1
    
    def order(self,first,start):
        for i in xrange(start+1,self.size):
            second = self.sumLength(start,i)
            if second == -1:return
            sumString =  str(first + second)
            if i + len(sumString) > self.size:return
            if sumString == self.num[i:i+len(sumString)]:
                if i + len(sumString) == self.size:
                    self.result = True
                    return
                self.order2(second,int(sumString),i+len(sumString))
    def order2(self,first,second,start):
        sumString = str(first+second)
        if start + len(sumString) > self.size or self.num[start] == '0':return
        third = self.num[start:start+len(sumString)]
        if sumString == third:
            if start + len(sumString) == self.size:
                self.result = True
                return
            self.order2(second,int(third),start + len(sumString))
                
