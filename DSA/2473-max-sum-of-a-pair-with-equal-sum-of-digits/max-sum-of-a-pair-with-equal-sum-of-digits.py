class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        # function to calculate the sum of digits
        def sum_of_digits(x):
            my_sum = 0
            while x>0:
                d = x % 10
                my_sum = my_sum + d
                x = x // 10
            return my_sum
        
        def find_largest_pair_sum(y):
            if len(y) < 2:
                return y[0]
            else:
                y.sort(reverse=True) #O(N log N)
                return y[0]+y[1]

        # key: sum of digits
        # value: all numbers that map to same sum of digits
        hashset = dict()

        # default
        max_sum = -1

        for i in nums:
            s = sum_of_digits(i)
            if s in hashset:
                hashset[s].append(i)
                total_sum = find_largest_pair_sum(hashset[s])
                max_sum = max(max_sum,total_sum)
            else:
                hashset[s] = [i]
        return max_sum

        