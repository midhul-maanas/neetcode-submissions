class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [0] * n
        for i in range(n):
            temp = max(prices[i:]) - prices[i]
            profit[i] = max(profit[i], temp)
        print(profit)
        return max(profit)