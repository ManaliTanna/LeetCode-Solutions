class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency = {}
        answer = set()
        for i in nums:
            if i in frequency:
                frequency[i] = frequency[i] + 1
            else:
                frequency[i] = 1
            if frequency[i] > math.floor(len(nums)/3):
                answer.add(i)
        return answer
        