class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # aCount = sum(1 for ch in s if ch == 'a')
        aCount = s.count('a')

        minDeletions = n
        bCount = 0
        # Second pass: iterate through the string to compute minimum deletions
        for ch in s:
            if ch == 'a':
                aCount -= 1

            minDeletions = min(minDeletions, aCount + bCount)
            if ch == 'b':
                bCount += 1
        
        return minDeletions
