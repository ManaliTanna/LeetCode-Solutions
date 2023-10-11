class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lptr = 0
        rptr = len(s)-1
        s = s.lower()
        s = s.replace(" ","")
        s = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), s))
        if (s[::-1] == s):
            return True
        else:
            return False