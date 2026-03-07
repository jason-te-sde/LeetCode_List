class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        # end condition
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            # illgal choices
            if used[i]:
                continue
            # make a decision
            track.append(nums[i])
            used[i] = True
            # enter into next decision tree
            self.backtrack(nums, track, used)
            # cancel choices
            track.pop()
            used[i] = False
        