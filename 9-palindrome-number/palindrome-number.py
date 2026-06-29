class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Edge cases
        if x < 0: #negative case 
            return False

        if x % 10 == 0 and x != 0:  #eg:- 100,10 etc
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return reverse == original
        
        