class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        current_sum = 0
        no_of_odd_sums_seen = 0
        no_of_even_sums_seen = 0
        total_count = 0
        for i in arr:
            current_sum = current_sum + i
            #even sum
            if current_sum%2==0:
                # to total count add all the count odd sums seen so far
                total_count = (total_count + no_of_odd_sums_seen) % (10**9 + 7)
                no_of_even_sums_seen = no_of_even_sums_seen + 1
            #odd sum
            else:
                # to total count add itself and all the count even sums seen so far
                total_count = (total_count + no_of_even_sums_seen + 1)  % (10**9 + 7)
                no_of_odd_sums_seen = no_of_odd_sums_seen + 1
        return total_count


        # Brute Force
        # count = 0
        # for i in range(len(arr)+1):
        #     for j in range(i+1,len(arr)+1):
        #         print(arr[i:j])
        #         if (sum(arr[i:j])%2!=0):
        #             count = count + 1
        # return count


        