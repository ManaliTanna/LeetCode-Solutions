class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        no_of_pairs = 0
        hashmap = defaultdict(int)
        good_pairs = 0
       
        for i in range(n):
            no_of_pairs = no_of_pairs + i
            # y = mx + c
            # if m is slpe=1
            # c = y - x
            # Grop all points that have same intercept togther.
            c = nums[i] - i
            # all previous occurrences of c form a good pair with the current element
            good_pairs = good_pairs + hashmap[c]
            hashmap[c] +=  1     
        return no_of_pairs - good_pairs


        # Time limit exceeded
        # n = len(nums)

        # #Total pairs
        # no_of_pairs = n * (n-1)/2
        # # print(no_of_pairs)

        # count = 0

        # #Find pair that is correct
        # i = 0
        # while i < len(nums):
        #     j = i
        #     while j < len(nums):
        #         print(i,j)
        #         if nums[i] - i == nums[j] - j and i!=j:
        #             count = count + 1
        #             # print(nums[i],i,nums[j],j)
        #         j = j + 1
        #     i = i + 1

        
        # return no_of_pairs - count