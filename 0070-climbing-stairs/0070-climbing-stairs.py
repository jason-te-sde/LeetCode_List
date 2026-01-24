class Solution:
    def climbStairs(self, n: int) -> int:
        """
        TC:O(n)
        SC:O(1)
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            thrid = first + second
            first = second
            second = thrid
        return second
