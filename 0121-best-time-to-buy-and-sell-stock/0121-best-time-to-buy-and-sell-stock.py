class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        using 2 loops to find the max_profit
        prices[j] - prices[i] find all possibility
        TC: O(n^2)
        SC: O(1)
        """
        """
        find min_price in one loop
        buy before sell
        min_price before max_price
        prices[i] - min_price
        find the max_profit
        TC: O(n)
        SC: O(1)
        """
        # define min_price use max number, define max_profit with 0
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            # update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            # calculate and update max_profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit