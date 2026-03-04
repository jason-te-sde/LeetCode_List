class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O(min(n, k))
        """
        max_length = 0
        left, right = 0, 0
        window = {}
        while right < len(s):
            c = s[right]
            right += 1
            # expend window
            window[c] = window.get(c, 0) + 1
            # shrink window
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            max_length = max(max_length, right - left)
        return max_length