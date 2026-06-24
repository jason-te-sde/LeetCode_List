class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
            tag : stack
            tc. : O(n)
            sc. : O(n)
        """
        stack = []
        for ops in operations:
            if ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(stack[-1] * 2)
            elif ops == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ops))
        return sum(stack)