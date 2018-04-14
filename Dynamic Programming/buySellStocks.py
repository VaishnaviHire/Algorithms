#attribution: www.leetcode.com
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_value = 0
        min_value = float('inf')
        
        for p in prices:
            min_value = min(min_value,p)
            profit = p - min_value
            max_value = max(max_value, profit)
        
        return max_value
    
                