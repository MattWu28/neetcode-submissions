class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for p in prices[1:]:
            if p < min_price:
                min_price = p
                continue
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit