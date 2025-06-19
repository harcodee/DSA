class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count = 1  # at least one group is needed
        start = nums[0]  # first element in the current group

        for num in nums:
            if num - start > k:
                count += 1
                start = num  # start a new group

        return count

        