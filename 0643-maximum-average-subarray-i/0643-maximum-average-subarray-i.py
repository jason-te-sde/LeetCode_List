class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            tag: sliding window
            tc : O(n)
            sc : o(k)
        """
        total = sum(nums[:k])
        max_total = total
        left = 0
        for right in range(k, len(nums)):
            total -= nums[left]
            total += nums[right]

            max_total = max(max_total, total)
            left += 1

        return max_total / k


