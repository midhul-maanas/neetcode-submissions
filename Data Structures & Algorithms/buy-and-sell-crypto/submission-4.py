class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0,0
        n = len(prices)
        while l < n:
            
            if r < n:
                profit = max(profit,prices[r] - prices[l])
                r+=1
            else:
                l += 1
                r = l + 1
        return profit

         