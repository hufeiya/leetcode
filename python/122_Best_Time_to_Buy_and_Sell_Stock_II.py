class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        money = 0
        for i in xrange(1,len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                money += profit
        return money
