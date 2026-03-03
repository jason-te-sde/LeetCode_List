class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        m = len(strs)
        n = len(strs[0])
        for col in range(n):
            for row in range(1, m):
                thisStr, prevStr = strs[row], strs[row - 1]
                if col >= len(thisStr) or col >= len(prevStr) or prevStr[col] != thisStr[col]:
                    return thisStr[:col]
        return strs[0]
        