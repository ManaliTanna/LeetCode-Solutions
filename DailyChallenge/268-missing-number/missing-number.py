class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != 0:
            return 0
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
        #print(nums)
        prev = nums[0]
        for i in nums[1:]:
            if i != prev+1:
                print(prev, i)
                return prev+1
            prev = i
        return i+1
        