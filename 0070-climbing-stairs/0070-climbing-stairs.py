class Solution:
    def climbStairs(self, n: int) -> int:
        """
            Tag: dynamic programming
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if n <= 2:
            return n
        
        
        dp1, dp2 = 1, 2
        for i in range(3, n + 1):
            temp = dp1 + dp2
            dp1 = dp2
            dp2 = temp
        return dp2