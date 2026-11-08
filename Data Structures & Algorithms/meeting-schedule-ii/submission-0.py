"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        prev = intervals[0].end
        room = 1

        for curr in intervals[1:]:
            if curr.start < prev:
                room += 1
            
            prev = curr.end   

        return room         