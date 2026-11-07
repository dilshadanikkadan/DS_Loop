"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        sorted(intervals,key=lambda x : x.start)

        prev = intervals[0].end
        for curr in intervals[1:]:
            print(curr.start,curr.end)
            if curr.end < prev:
                return False

        return True        