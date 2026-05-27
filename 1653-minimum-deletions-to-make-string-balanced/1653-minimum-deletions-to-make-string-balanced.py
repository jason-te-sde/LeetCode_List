class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
            tag : DP
            tc  : O(n)
            sc  : O(n)
        """
        n = len(s)
        dp = [0] * (n + 1)
        bCount = 0

        # dp[i]: The number of deletions required to
        # balance the substring s[0, i)

        for i in range(n):
            if s[i] == 'b':
                dp[i + 1] = dp[i]
                bCount += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                dp[i + 1] = min(dp[i] + 1, bCount)
        
        return dp[n]