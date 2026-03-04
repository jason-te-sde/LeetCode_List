class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, need = {}, {}
        left, right = 0, 0
        valid = 0
        max_length = float("inf")
        res = ""
        
        for c in t:
            need[c] = 1 + need.get(c, 0)

        while right < len(s):
            c = s[right]      
            window[c] = window.get(c, 0) + 1
            
            if c in need and need[c] == window[c]:
                valid += 1
            
            while valid == len(need):
                if right - left + 1 < max_length:
                    res = s[left : right + 1]
                    max_length = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    valid -= 1
                left += 1
            right += 1

        return res if max_length != float("inf") else ""
            



        