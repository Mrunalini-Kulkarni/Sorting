# Leetcode 2706.Buy Two Chocolates

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(len(prices) - 1):
            if prices[i] + prices[i + 1] <= money:
                return money - prices[i] - prices[i + 1]
        return money