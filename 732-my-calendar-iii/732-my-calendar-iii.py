import bisect
class MyCalendarThree:

    def __init__(self):
        self.event_starts = []
        self.event_ends = []
        self.k = 0
    def book(self, start: int, end: int) -> int:
        y, x = bisect.bisect_left(self.event_starts, end), bisect.bisect_right(self.event_ends, start)
        point1 = x
        k = 1
        for point2 in range(x, y):
            if self.event_starts[point2]<self.event_ends[point1]:
                k +=1
            else:
                point1 += 1
        self.k = max(k, self.k)
        bisect.insort(self.event_starts, start)
        bisect.insort(self.event_ends, end)
        return self.k