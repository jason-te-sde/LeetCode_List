class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            tag : dp
            tc  : O(n^2)
            sc. : O(n)
        """
        if not nums:
            return 0

        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            res = max(dp[i], res)

        return res
    