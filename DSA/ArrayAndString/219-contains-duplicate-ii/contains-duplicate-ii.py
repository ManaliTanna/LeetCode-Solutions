class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()

        l_ptr = 0

        for r_ptr in range(len(nums)):

            # slide window to the left
            if r_ptr - l_ptr > k:
                window.remove(nums[l_ptr])
                l_ptr = l_ptr + 1
            
            # if value already exists in window, found duplicate!
            if nums[r_ptr] in window:
                return True

            window.add(nums[r_ptr])

        return False


        