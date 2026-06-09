class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            tag: sliding window
            tc : O(n)
            sc : O(1)
        """
        total = sum(nums[:k])
        max_total = total
        for right in range(k, len(nums)):
            total -= nums[right - k]
            total += nums[right]

            max_total = max(max_total, total)

        return max_total / k


