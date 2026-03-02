class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time complexity : O(n)
        space complexity: O(1)
        """
        if len(nums) == 0:
            return 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1
        