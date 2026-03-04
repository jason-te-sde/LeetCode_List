class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            Time Complexity: O(s)
            Space Complexity: O(p)
        """
        res = []
        left, right = 0, 0
        valid = 0
        need, window = {}, {}
        
        for c in p:
            need[c] = need.get(c, 0) + 1
        
        while right < len(s):
            c = s[right]
            right += 1
            # expend window
            if c in need:
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    valid += 1
            # shrink window
            while right - left >= len(p):
                # update res
                if valid == len(need):
                    res.append(left)
                # move left
                d = s[left]
                left += 1
                # delete element in window
                if d in need:
                    # if d is in need and number is match, valid - 1
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


        
        
        