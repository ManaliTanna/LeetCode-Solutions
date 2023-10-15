class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #two pointer approach, keep adding from right and remove from left if duplicate, clear and to the set at each point, store max count
        l_ptr = 0
        r_ptr = 0
        my_set = set()
        max_len = 0
        while r_ptr < len(s):
            while s[r_ptr] in my_set:
                my_set.remove(s[l_ptr])
                l_ptr = l_ptr + 1
            my_set.add(s[r_ptr])
            my_len = r_ptr - l_ptr + 1
            max_len = max(max_len, my_len)
            r_ptr = r_ptr + 1
        return max_len

        

 

