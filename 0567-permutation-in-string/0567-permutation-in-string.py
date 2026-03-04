class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Time Complexity : O(len(s2))
            Space Complexity: O(1)
        """
        left, right = 0, 0
        have, need = {}, {}
        valid = 0
        
        for c in s1:
            need[c] = 1 + need.get(c, 0)
        
        while right < len(s2):
            c = s2[right]
            right += 1
            # expend window
            if c in need:
                have[c] = 1 + have.get(c, 0)
                if have[c] == need[c]:
                    valid += 1
            # shrink window
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                delete_element = s2[left]
                left += 1
                if delete_element in need:
                    if have[delete_element] == need[delete_element]:
                        valid -= 1
                    have[delete_element] -= 1
        return False
                    
                    

