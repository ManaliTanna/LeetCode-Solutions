class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=n
        if x == 1 or x == 2:
            return True
        if x == 0:
            return False
        while x>2:
            if x%2 != 0:
                return False
            x = x/2
        if x==2:
            return True
        else:
            return False



        