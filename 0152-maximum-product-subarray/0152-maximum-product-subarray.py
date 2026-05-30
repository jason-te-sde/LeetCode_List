class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            tag: DP
            tc : O(n)
            sc : O(1)
        """
        res = nums[0]

        curMax = nums[0]
        curMin = nums[0]

        for num in nums[1:]:
            tempMax = curMax

            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, tempMax * num, curMin * num)

            res = max(res, curMax)
        
        return res

        