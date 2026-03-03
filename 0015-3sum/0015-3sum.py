class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            pairs = self.twoSum(nums[i + 1 : n], 0 - nums[i])
            for pair in pairs:
                pair.append(nums[i])
                res.append(pair)
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        lo = 0
        hi = len(nums) - 1
        res = []
        while lo < hi:
            left, right = nums[lo], nums[hi]
            if left + right < target:
                lo += 1
            elif left + right > target:
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res
        