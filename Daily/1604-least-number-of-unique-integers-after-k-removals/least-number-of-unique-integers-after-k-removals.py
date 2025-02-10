class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        frequency = {}
        for i in arr:
            frequency[i] = frequency.get(i, 0) + 1

        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1])

        to_remove = set()
        for key, value in sorted_frequency:
            if k - value < 0:
                break
            to_remove.add(key)
            k -= value

        return len(set(arr) - to_remove)