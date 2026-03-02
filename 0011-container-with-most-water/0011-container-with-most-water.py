class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                res = max(res, leftMax * (right - left))
                left += 1
            else:
                res = max(res , rightMax * (right - left))
                right -= 1
        return res
        