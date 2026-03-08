class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res
    
    def backtrack(self, nums: List[int]) -> None:
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return
        
        for i in range(len(nums)):
            if self.used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            
            self.track.append(nums[i])
            self.used[i] = True

            self.backtrack(nums)
            
            self.track.pop()
            self.used[i] = False

        