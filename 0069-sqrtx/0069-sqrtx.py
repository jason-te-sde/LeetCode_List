class Solution:
    def mySqrt(self, x: int) -> int:
        """
            tag: binary search
            time complexity: O(logn)
            space complexity: O(1)
        """

        if x < 2:
            return x
        
        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        
        return right

        