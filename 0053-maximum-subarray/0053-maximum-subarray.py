class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            tag : DP
            tc. : O(n)
            sc. : O(1)
        """
        maxSum = nums[0]
        curSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        
        return maxSum
