class Solution:
    def climbStairs(self, n: int) -> int:
        """
        TC:O(logN)
        SC:O(1)
        """
        sqrt5 = 5 ** 0.5
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt5)
