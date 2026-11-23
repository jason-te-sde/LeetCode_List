class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res = float("-inf")
        cur = 0
        for i, right in enumerate(nums):
            # 1. in
            cur += right
            
            left = i - k + 1
            if left < 0:
                continue
            
            # 2. update
            res = max(res, cur)

            # 3. out
            cur -= nums[left]
        
        return res / k
            