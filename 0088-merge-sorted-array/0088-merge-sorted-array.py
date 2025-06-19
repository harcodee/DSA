class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
       

        # Start from the end of nums1 and nums2
        i = m - 1  # Last valid element in nums1
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1

        # Merge nums2 into nums1 from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2 (nums1 is already there)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        

        