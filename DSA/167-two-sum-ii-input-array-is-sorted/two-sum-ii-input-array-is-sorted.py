class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)

        l_ptr = 0
        r_ptr = n-1

        while l_ptr<r_ptr and l_ptr<n and r_ptr>0:
            my_sum = numbers[l_ptr]+numbers[r_ptr]
            if  my_sum == target:
                return [l_ptr+1,r_ptr+1]
            elif my_sum < target: 
                l_ptr = l_ptr + 1
            else:
                r_ptr = r_ptr - 1

        