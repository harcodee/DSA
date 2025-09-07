class Solution:
    def evenlyDivides(self, n):
        count = 0
        num = str(n)   
        
        for i in num:
            if (int(i)==0):
                continue
            elif (n%int(i) == 0):
                count += 1
        return count