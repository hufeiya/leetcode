class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        lowest = prices[0]
        max = 0
        for i in xrange(1,len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i] - lowest > max:
                max = prices[i] - lowest
        return max
