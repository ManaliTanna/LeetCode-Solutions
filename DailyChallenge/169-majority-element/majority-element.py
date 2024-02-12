import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        target_frequency = math.floor(len(nums) / 2)
        print(target_frequency)
        for i in nums:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1
            if frequency[i] > target_frequency:
                    return i
        

        