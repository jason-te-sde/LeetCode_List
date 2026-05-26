class Solution:
    def minimumDeletions(self, s: str) -> int:
        charStack = []
        deleteCount = 0

        # Iterate through each character in the string
        for char in s:
            # If stack is not empty, top of stack is 'b',
            # and current char is 'a'

            if charStack and charStack[-1] == "b" and char == "a":
                charStack.pop() # Remove 'b' from stack
                deleteCount += 1 # Increment deletion count
            else:
                charStack.append(char) # Append current character to stack
        
        return deleteCount