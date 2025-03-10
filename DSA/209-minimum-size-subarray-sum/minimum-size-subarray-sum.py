class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # if entire array does not sum up to target or greater return 0
        if sum(nums) < target:
            return 0

        # 2 pointers to track subarray
        l_ptr = 0
        r_ptr = 0

        n = len(nums)
        my_sum = 0

        # store the length of minimal subarray
        minimal_len = float('inf')

        # iterate end of array
        while r_ptr<n:

            # add element to the window from the right side and calculate sum
            my_sum = my_sum + nums[r_ptr]
            r_ptr = r_ptr + 1

            # if sum is greater than target, store minimal length
            # remove left element from the window
            while my_sum >= target:
                minimal_len = min(minimal_len, r_ptr - l_ptr)
                my_sum = my_sum - nums[l_ptr]
                l_ptr = l_ptr + 1
        
        return minimal_len


        