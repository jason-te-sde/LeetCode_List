class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            tag: Greedy
            tc : O(n)
            sc : O(1)
        """
        n = len(nums)
        jumps = 0
        curFarthest = 0
        curEnd = 0

        for i in range(n - 1):
            curFarthest = max(curFarthest, i + nums[i])
            
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
        
        return jumps
