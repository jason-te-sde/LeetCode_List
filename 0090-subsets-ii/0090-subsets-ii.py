class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: Linst[int], start: int) -> None:
        self.res.append(self.track[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i + 1)
            self.track.pop()