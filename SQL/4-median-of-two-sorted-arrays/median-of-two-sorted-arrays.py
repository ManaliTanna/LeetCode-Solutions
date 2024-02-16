import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_arr = []
        n = len(nums1)+len(nums2)
        sorted_arr = nums1 + nums2
        print(sorted_arr)
        sorted_arr.sort()
        print(sorted_arr)

        if n % 2 == 0:
            middle_left = sorted_arr[n // 2 - 1]
            middle_right = sorted_arr[n // 2]
            return float((middle_left + middle_right)) / 2
        else:
            return sorted_arr[n // 2]
        