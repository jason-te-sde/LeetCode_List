class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            tag: dynamic programming
            time complexity: O(m * n)
            space complexity: O(n)
            n = amount, m = len(coins)
        """

        if amount == 0: # edge case 1
            return 0
        if amount < 0: # edge case 2
            return -1
        # the maxium number of coins of amount is amount + 1, which means coin denomination is 1, then add 1
        dp = [amount + 1] * (amount + 1)
        # init
        dp[0] = 0

        for i in range(1, len(dp)): # bottom -> top
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        

