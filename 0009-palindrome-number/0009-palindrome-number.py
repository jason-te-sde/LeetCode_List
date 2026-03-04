class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        y = 0
        while temp > 0:
            last_num = temp % 10
            temp = temp // 10
            y = 10 * y + last_num
        
        return True if y == x else False