class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            tag : two pointers
            tc. : O(nlogn)
            sc. : O(n)
        """
        pairs = [(value, index) for index, value in enumerate(nums)]
        pairs.sort()
        left, right = 0, len(pairs) - 1
        while left < right:
            res = pairs[left][0] + pairs[right][0]
            if res < target:
                left += 1
            elif res > target:
                right -= 1
            else:
                return[pairs[left][1], pairs[right][1]]
        