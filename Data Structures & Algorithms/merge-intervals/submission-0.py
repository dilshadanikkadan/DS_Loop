class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for curr in intervals[1:]:

            prev = res[-1]

            if curr[0] <= prev[1]:
                prev[1] = max(curr[1],prev[1])
            else:
                res.append(curr)    

        return res