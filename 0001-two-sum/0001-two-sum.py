class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        brute force
        one is i
        the other is j
        find i + j == target
        O(n^2)
        """
        """
        save nums[i] in hashmap
        find the target - nums[i]
        return[i, hashmap[target- nums[i]]]
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            # can't find it, return []
        return[]
        