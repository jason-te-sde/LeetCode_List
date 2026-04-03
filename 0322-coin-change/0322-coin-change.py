class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2] * (amount + 1)
    
        def dp(coins: List[int], amount:int) -> int:
            if amount == 0: return 0 # base case   
            if amount < 0: return -1 # edge case
            if memo[amount] != -2: return memo[amount] # check the memo to prevent redundant calculations
                
            
            res = float('inf') # return minimum, so init maximum
            for coin in coins:# top -> bottom
                # calcluate the result of the sub-problem
                subProblem = dp(coins, amount - coin)
                # skip if the sub-problem has no solution
                if subProblem == -1:
                    continue
                res = min(res, subProblem + 1) # add current coin

            memo[amount] = res if res != float('inf') else -1
            return memo[amount]
            
        return dp(coins, amount)
            

