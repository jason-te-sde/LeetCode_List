class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp1, dp2 = 0, 1
        for i in range(2, n + 1):
            dpi = dp1 + dp2
            dp1 = dp2
            dp2 = dpi
        
        return dp2