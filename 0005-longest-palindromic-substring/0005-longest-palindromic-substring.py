class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            tag: two pointers
            tc : O(n^2)
            sc : O(n)
        """

        self.res = ""
        self.resLen = 0

        for i in range(len(s)):
            # odd length
            self.isPalindorme(s, i, i)

            # even length
            self.isPalindorme(s, i, i + 1)

        return self.res
            
    
    def isPalindorme(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > self.resLen:
                self.res = s[l : r + 1]
                self.resLen = r - l + 1
            r += 1
            l -= 1

            
