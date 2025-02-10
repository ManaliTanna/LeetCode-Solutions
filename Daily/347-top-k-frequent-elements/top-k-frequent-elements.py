class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # General Algorithm for top K --> even in big data
        # Find frequency
        # Keep counts as index
        # Then find top k based on the counts

        frequency = {}
        counts = [[] for i in range (len(nums) + 1)]

        # create a frequency hashmap
        for i in nums:
            frequency[i] = 1 + frequency.get(i,0)

        # create array with count as index
        for num, count in frequency.items():
            counts[count].append(num)

        result = []

        # Traverse counts array and find top k
        for num_list in range(len(counts) - 1 , 0 , -1):
            for each_num in counts[num_list]:
                result.append(each_num)
                if len(result) == k:
                    return result
