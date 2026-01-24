class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        n = nums.lenth
        m = maxvalue - minvalue
        TC: O(n+m) 
        SC: O(m)
        """
        # create a count array based on maxvalue and minvalue
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        
        # find the kth largest element
        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value
        
        # if can't find, return -1
        return -1
        



        