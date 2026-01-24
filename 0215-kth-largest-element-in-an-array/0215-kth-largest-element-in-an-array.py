class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        n = nums.length
        m = max_value - min_value = count.size
        TC: O(n + m)
        SC: O(m)
        """
        # create a count array for each elements
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        # find the kth largest element in count array in reverse way
        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return min_value + num
        # can't find, return -1
        return -1
        



        