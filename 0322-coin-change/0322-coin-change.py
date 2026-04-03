class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dp(rem):
            if rem == 0: return 0
            if rem < 0: return -1

            res = float('inf')
            for coin in coins:
                subProblem = dp(rem - coin)
                if subProblem != -1:
                    res = min(res, subProblem + 1)
            return res if res != float('inf') else -1
        
        return dp(amount)