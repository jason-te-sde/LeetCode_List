class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            tag : DP
            tc. : O(n * k^2) 
            sc. : O(n + m * k)
        """
        longestWord = 0
        for word in wordDict:
            longestWord = max(longestWord, len(word))
            
        wordSet = set(wordDict)

        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i - 1, max(-1, i - longestWord - 1), -1):
                if dp[j] and s[j : i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[-1]

        