class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        i=1
        prefix = 1
        while i<len(nums):
            prefix = prefix * nums[i-1]
            res.append(prefix)
            i = i + 1
        print(res)
        j = len(nums)-2
        suffix = 1
        while j>=0:
            suffix = suffix * nums[j+1]
            print( nums[j+1],suffix,res[j])
            res[j] = res[j] * suffix
            j = j - 1
        return res
        # BRUTE
        # k = 0
        # res = []
        # while k<len(nums):
        #     prod = 1
        #     for i in range(len(nums)):
        #         if i!=k:
        #             prod = prod * nums[i]
        #     k = k + 1
        #     res.append(prod)
        # return res


        