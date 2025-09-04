class Solution:
    def evenlyDivides(self, n):
        count = 0
        num = n   
        
        while num > 0:
            digit = num % 10
            if digit != 0 and n % digit == 0:
                count += 1
            num //= 10   
        return count
