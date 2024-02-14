class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        sum = 0
        while n>0:
            d = n%10
            sum = sum*10 + d
            n = n/10
        if sum == x:
            return True
        else:
            return False