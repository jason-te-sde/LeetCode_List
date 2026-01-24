class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        """
        def check_palidrome(s, i , j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        # two pointers 
        i = 0
        j = len(s) - 1
        # check if it a palidrome
        while i < j:
            if s[i] != s[j]:
                # skip one element left or right, check palidrome again
                return check_palidrome(s, i + 1, j) or check_palidrome(s, i, j - 1)
            i += 1
            j -= 1
        return True
        
        