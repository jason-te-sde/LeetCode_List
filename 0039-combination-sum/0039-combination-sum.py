class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.trackSum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return res
        self.backtrack(candidates, 0, target)
        return self.res
    
    def backtrack(self, nums: List[int], start: int, target: int) -> None:
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        
        if self.trackSum > target:
            return 
        
        for i in range(start, len(nums)):
            self.trackSum += nums[i]
            self.track.append(nums[i])

            self.backtrack(nums, i, target)

            self.trackSum -= nums[i]
            self.track.pop()
        