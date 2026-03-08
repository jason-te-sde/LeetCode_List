class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.trackSum = 0
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        candidates.sort()
        self.backtrack(candidates, 0, target)
        return self.res
    
    def backtrack(self, candidates: List[int], start: int, target: int) -> None:
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        
        if self.trackSum > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.backtrack(candidates, i + 1, target)
            self.track.pop()
            self.trackSum -= candidates[i]

        