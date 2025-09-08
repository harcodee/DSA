class Solution:
    def gcd(self, a, b):
        # code here
        rem = 1
        if a>b:
            dividend = a
            divisor = b
        else:
            dividend = b
            divisor = a
        while rem!=0:
            rem = dividend%divisor
            if rem!=0:
                dividend = divisor
                divisor = rem
        return divisor    
                
            
        