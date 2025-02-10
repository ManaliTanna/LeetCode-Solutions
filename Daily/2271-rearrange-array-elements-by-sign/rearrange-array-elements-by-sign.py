class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        answer = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        #print(pos)
        #print(neg)
        ptr_p = 0
        ptr_n = 0
        for i in range(len(nums)):
            if i%2 == 0:
                answer.append(pos[ptr_p])
                ptr_p+=1
            else:
                answer.append(neg[ptr_n])
                ptr_n+=1
        return answer