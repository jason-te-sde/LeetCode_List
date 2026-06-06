class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
            tag : two pointers
            tc. : O(n)
            sc. : O(1)
        """
        n = len(nums)
        ans = [0] * n
        new_left = 0
        new_right = n - 1
        original_left = 0
        original_right = n - 1
        
        while original_left < n or original_right > 0:
            if nums[original_left] < pivot:
                ans[new_left] = nums[original_left]
                new_left += 1
            
            if nums[original_right] > pivot:
                ans[new_right] = nums[original_right]
                new_right -= 1 
            
            original_left += 1
            original_right -= 1
        
        while new_left <= new_right:
            ans[new_left] = pivot
            new_left += 1
        
        return ans

            
            

