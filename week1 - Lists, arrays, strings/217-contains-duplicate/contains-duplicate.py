class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueset = set()
        for i in nums:
            if i in uniqueset:
                return True
            else:
                uniqueset.add(i)
        return False