class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
            tag: prefix sum
            tc : O(n)
            sc : O(n)
        """
        n = len(nums)
        preSum = [0] * (n + 1)
        min_value = 1

        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
            if preSum[i] < 0 and abs(preSum[i]) >= min_value:
                min_value = -preSum[i] + 1
        
        return min_value