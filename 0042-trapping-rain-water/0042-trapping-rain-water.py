class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Time Complexity: O(n)
            Space Complecity: O(1)
        """
        left, right = 0, len(height) - 1
        res = 0
        leftMax, rightMax = 0, 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                res += leftMax - height[left]
                left += 1
            else:
                res += rightMax - height[right]
                right -= 1
        return res
        