class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.hashTable = {}
        return self.__isHappy(n)
    def __isHappy(self, n):
        m = str(n)
        sum = 0
        for i in m:
            sum += int(i)**2
        if sum == 1:
            return True
        elif sum in self.hashTable:
            return False
        else:
            self.hashTable[sum] = 0
            return self.__isHappy(sum)
