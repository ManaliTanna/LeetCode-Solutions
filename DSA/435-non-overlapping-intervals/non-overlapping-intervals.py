class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # len of intervals array
        n = len(intervals)

        # sort based on finishing time of all intervals
        intervals = sorted(intervals, key=lambda x: x[1])

        # print(intervals)

        # add first pair to result array
        # result = [intervals[0]]

        #keep track of finishing time of pair recently added to result
        finishing_time = intervals[0][1]

        count = 0

        # print(finishing_time)

        # iterate through array
        for i in range(1,n):

            # if the next element starts after the previously added element ends
            # add it to the result array
            # and keep track of its finishing time
            if intervals[i][0] >= finishing_time:
                # result.append(intervals[i])
                finishing_time = intervals[i][1]
            else:
                count = count + 1
        
        # print(result)
        return count
        # return n-len(result)


