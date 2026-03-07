class Solution:
    """
        Time Complexity = O(n! / (k-1)! * (n-k)!)
        Space Complexity = O(k)
    """
    def __init__(self):
        self.res = []
        self.track = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.res

    def backtrack(self, n: int, k: int, start: int) -> None:
        if k == len(self.track):
            self.res.append(self.track.copy())
            return
        
        for i in range(start, n + 1):
            self.track.append(i)
            self.backtrack(n, k, i + 1)
            self.track.pop()
        