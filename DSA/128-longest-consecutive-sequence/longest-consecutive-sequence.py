class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set of all nums O(1)
        my_set = set(nums)

        #final answer
        count = 0

        # iterate O(n)
        for i in my_set:
            # if i-1 does not exist it could potentially be the start of a sequence
            if i-1 not in my_set:

                #start counting length of sequence
                seq_len = 0
                # as long as starting number + length exists in set, increment length
                while (i+seq_len) in my_set:
                    seq_len = seq_len + 1

                #consider max of current count and sequence length and set the new count
                count = max(count,seq_len)

        return count


            

        