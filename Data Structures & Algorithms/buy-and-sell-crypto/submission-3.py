class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        ans = 0
        r = 1  

        while r < len(prices):
            profit = 0
            if prices[r] < prices[L]:
                L += 1
                
            else:
                profit = prices[r] - prices[L]
                ans = max(ans, profit)
                r += 1
        return ans 

