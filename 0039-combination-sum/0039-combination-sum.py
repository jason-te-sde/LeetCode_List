class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        self.backtrack(candidates, 0, target, 0)
        return self.res
    
    def backtrack(self, candidates, start, target, sum):
        if sum == target:
            self.res.append(self.track.copy())
            return
        if sum > target:
            return

        for i in range(start, len(candidates)):
            self.track.append(candidates[i])
            sum += candidates[i]

            self.backtrack(candidates, i, target, sum)

            sum -= candidates[i]
            self.track.pop()


        