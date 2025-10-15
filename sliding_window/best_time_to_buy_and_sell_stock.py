#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://neetcode.io/solutions/best-time-to-buy-and-sell-stock

class SoluctionBestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        price_range = len(prices)
        while price_range > 1:
            maxIndexValue = prices.index(max(prices))
            minIndexValue = prices.index(min(prices))
            if maxIndexValue > minIndexValue:
                return prices[maxIndexValue] - prices[minIndexValue]
            else
                del prices[minIndexValue]
        return 0
