"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(0, i):
                if ((intervals[i].start >= intervals[j].start and intervals[i].start < intervals[j].end)
                    or (intervals[i].end > intervals[j].start and intervals[i].end <= intervals[j].end)
                    or (intervals[i].start <= intervals[j].start and intervals[i].end >= intervals[j].end)):
                    return False

        return True