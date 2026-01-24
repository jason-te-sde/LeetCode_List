class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
# 1. First pass: Clean up all extra closing parentheses ')' from left to right.
        s = self.delete_invalid_closing(s, "(", ")")
# 2. Second pass: Reverse the string and remove extra opening parentheses '(' from the other direction.
        s = self.delete_invalid_closing(s[::-1], ")", "(")
        
# Reverse one last time to restore the original order.
        return s[::-1]
        
    
    def delete_invalid_closing(self, string, open_symbol, close_symbol):
        sb = []
        balance = 0
        for c in string:
# 3. Core Logic: Use a counter to track balance; skip (delete) any bracket that doesn't have a matching partner.
            if c == open_symbol:
                balance += 1
            if c == close_symbol:
                if balance == 0:
                    continue
                balance -= 1
            sb.append(c)
        return "".join(sb)