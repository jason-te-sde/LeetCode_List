class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            tag: two pointers
            tc.: O(n)
            sc.: O(1)
        """
        n = len(nums)

        slow = 0
        for fast in range(1, n):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1