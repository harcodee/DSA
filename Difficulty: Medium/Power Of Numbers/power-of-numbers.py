class Solution:
    def reverseexponentiation(self, n):
        # code here
        rev = 0
        temp = n
        while temp > 0 :
            r = temp % 10
            rev = rev * 10 + r
            temp //= 10
        
        
        return n ** rev   