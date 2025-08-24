class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = second =-1
        
        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num!= largest:
                second = num
        return second