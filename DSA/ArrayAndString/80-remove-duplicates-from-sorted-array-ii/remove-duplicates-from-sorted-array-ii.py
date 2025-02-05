class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_ptr = 0 # tracks the 2 positions to shift to
        # l only moves two at a time
        r_ptr = 0 # tracks the 2 positions (second set of non duplicates) that need to be shifted

        while r_ptr < len(nums):
            count = 1

            # count duplicates (equal to next number)
            # goes till end of duplicate
            # it matters that r_ptr + 1 < len(nums) condition comes before the 2nd condition!
            while r_ptr + 1 < len(nums) and nums[r_ptr] == nums[r_ptr+1]:
                r_ptr = r_ptr + 1
                count = count + 1

            # shift values the number of times needed
            for i in range(min(2, count)):
                nums[l_ptr] = nums[r_ptr]
                l_ptr = l_ptr + 1

            r_ptr = r_ptr + 1
            
        return l_ptr



                
