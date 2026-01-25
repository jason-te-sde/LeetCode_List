class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        [substitution]
        sub7on
        s10n
        s010n
        word.length <= 20
        abbr.length <= 10
        1 <= number <= 20 
        """
        # compare word with abbr
        i = j = 0
        n, m = len(word), len(abbr)
        while i < n and j < m:
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                k = j
                while k < m and abbr[k].isdigit():
                    k += 1
        # if meet digits in abbr, we skip the length of it in word
                i += int(abbr[j:k])
                j = k
            else:
                return False
        # compare the length
        return i == n and j == m
        
                

        
        