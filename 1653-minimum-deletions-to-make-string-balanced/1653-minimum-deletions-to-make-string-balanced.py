class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        countA = [n] * n
        Acount = 0

        # First pass: compute countA which stores the number of 
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            countA[i] = Acount
            if s[i] == 'a':
                Acount += 1
        
        minDeletions = n
        Bcount = 0
        # Second pass: compute minimum deletions on the fly
        for i in range(n):
            minDeletions = min(countA[i] + Bcount, minDeletions)
            if s[i] == 'b':
                Bcount += 1
        
        return minDeletions