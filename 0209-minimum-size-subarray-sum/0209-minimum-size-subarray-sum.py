class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            tag : sliding window
            tc  : O(n)
            sc. : O(1)
        """
        left = 0
        right = 0
        windowSum = 0
        res = float('inf')

        while right < len(nums):
            windowSum += nums[right]
            right += 1
            while windowSum >= target and left < right:
                res = min(res, right - left)
                windowSum -= nums[left]
                left += 1
        
        return 0 if res == float('inf') else res