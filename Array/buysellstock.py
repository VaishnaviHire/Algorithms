#attribution: www.leetcode.com
# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as 
# you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage 
# in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if prices == []:
            return 0
        if len(prices) == 1:
            return 0
        else:
            buy_price = 0
            sell_price = 0
            profit = 0
            has_stock = False
            for i in range(len(prices)-1):
                if prices[i] < prices[i+1] and has_stock == False:
                    has_stock =True
                    buy_price = prices[i]

                if prices[i] > prices[i+1] and has_stock:
                    has_stock = False
                    sell_price = prices[i]
                    profit += sell_price - buy_price
                    sell_price = 0
                    buy_price = 0
                
                if prices[i] < prices[i+1] and has_stock:
                    has_stock = False
                    sell_price = prices[i+1]
                    profit += sell_price - buy_price
                    sell_price = 0
                    buy_price = 0
                    

            return profit