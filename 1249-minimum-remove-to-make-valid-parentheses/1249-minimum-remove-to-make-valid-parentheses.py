class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        TC:O(n)
        SC:O(n)
        """
        # 1 pass : clean up extra invalid ")"
        s = self.delete_invalid_closing(s, "(", ")")

        # 2 pass : clean up extra invalid "("
        s = self.delete_invalid_closing(s[::-1], ")", "(")

        # revsed to restore the original string
        return s[::-1]

    def delete_invalid_closing(slef, string, open_symbol, close_symbol):
        sb = []
        balance = 0 # match "()"
        for c in string:
            if c == open_symbol:
                balance += 1
            elif c == close_symbol:
                if balance == 0:
                    continue
                balance -= 1
            sb.append(c)
        return "".join(sb)
        