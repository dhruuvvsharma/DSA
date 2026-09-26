class Solution:
    def isHappy(self, n: int) -> bool:
        def Square_Sum(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10
            return total

        slow = n
        fast = n
        while fast !=1:
            slow = Square_Sum(slow)
            fast = Square_Sum(Square_Sum(fast))

            if slow == fast and slow !=1:
                return False
        return True


