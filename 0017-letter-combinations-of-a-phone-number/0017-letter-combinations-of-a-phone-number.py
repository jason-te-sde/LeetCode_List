class Solution:
    """
        tag: backtracking
        Time Complexity: O(4^n * n)
        Space Complexity: O(n)
    """

    mappings = [
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ]

    def __init__(self):
        self.res = []
        self.track = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.res
        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits: str, start: int) -> None:
        if len(self.track) == len(digits):
            self.res.append(''.join(self.track))
            return

        digit = ord(digits[start]) - ord('0')
        for c in self.mappings[digit]:
            self.track.append(c)
            self.backtrack(digits, start + 1)
            self.track.pop()

        