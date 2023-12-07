class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(filter(lambda x: x.isalnum(), s))
        if (s[::-1] == s):
            return True
        else:
            return False