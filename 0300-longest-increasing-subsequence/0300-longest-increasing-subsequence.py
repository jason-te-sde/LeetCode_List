class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            tg : greedy + bisect
            tc : O(nlogn)
            sc : O(n)
        """
        tails = []

        for num in nums:
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)
