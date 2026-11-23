class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = cur = 0
        vowels = "aeiou"
        
        for i, c in enumerate(s): # right 
            if c in vowels:
                # 1. in
                cur += 1
            
            left = i - k + 1
            if left < 0:
                continue
            
            # 2. update
            res = max(cur, res)
            if res == k:
                break

            # 3. out
            if s[left] in vowels:
                cur -= 1
        
        return res

            

            
        
        