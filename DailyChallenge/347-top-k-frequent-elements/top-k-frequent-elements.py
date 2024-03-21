class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Sorting the dictionary items by frequency
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # Extracting the k most frequent elements
        return [element[0] for element in sorted_frequency[:k]]