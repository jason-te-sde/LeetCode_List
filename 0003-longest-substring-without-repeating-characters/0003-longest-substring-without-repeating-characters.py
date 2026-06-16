class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            tag: sliding window
            tc : O(n)
            sc : O(n)
        """
        left = 0
        max_length = 0
        last_seen = {}
        
        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            
            last_seen[c] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
