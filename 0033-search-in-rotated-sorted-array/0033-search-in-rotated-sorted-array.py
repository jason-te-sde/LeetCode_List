class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            Tag: Binary Search
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        # find the index of the pivot element(the smallest element)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        res = self.binarySearch(nums, 0, left - 1, target)
        if res != -1:
            return res
        
        return self.binarySearch(nums, left, len(nums) - 1, target)
    
    def binarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        