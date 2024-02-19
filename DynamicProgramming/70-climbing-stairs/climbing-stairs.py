class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways_taking_one_step = 1
        ways_taking_two_step = 1

        for i in range(n-1):

            temp = ways_taking_one_step

            #Caluclate total no. of ways the next 
            ways_taking_one_step = ways_taking_one_step + ways_taking_two_step

            #update for next iteration
            ways_taking_two_step = temp

        return ways_taking_one_step


        