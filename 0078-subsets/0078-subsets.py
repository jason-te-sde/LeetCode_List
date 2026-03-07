class Solution:
    """
        Time Complexity : O(n * 2^n)
        Space Complexity : O(n * 2^n)
    """
    def __init__(self):
        self.res = []
        self.track = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: List[int], start: int) -> None:
        # preorder, everu node's value is a subset
        self.res.append(list(self.track))

        for i in range(start, len(nums)):
            # make a choice
            self.track.append(nums[i])
            # use start parameter to contorl the traversal of tree, avoid repeating subsets
            self.backtrack(nums, i + 1)
            # withdraw choices
            self.track.pop()
        