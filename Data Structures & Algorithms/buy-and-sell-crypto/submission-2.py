class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                # max_profit = max(profit, max_profit)
                if profit < 0:
                    j - i
                max_profit = max(profit, max_profit)


        return max_profit
