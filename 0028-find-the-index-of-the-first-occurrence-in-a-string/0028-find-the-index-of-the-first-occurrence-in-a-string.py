class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window + i]:
                    break
                if i == m - 1:
                    return window
        return -1
        