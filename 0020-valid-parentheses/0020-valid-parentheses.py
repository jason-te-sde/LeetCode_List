class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in mappings:
                if stack and mappings[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        