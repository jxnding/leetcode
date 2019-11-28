# My solution:
class MyCalendarTwo:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        def overlap(a, b):
            if a==[] or b==[]:
                return []
            if a[0]>=b[1]:
                return []
            if a[1]<=b[0]:
                return []
            return [max(a[0],b[0]), min(a[1],b[1])]
        self.cal.sort()

        #first pass
        overlaps = []
        for i in range(len(self.cal)):
            if overlap(self.cal[i], [start,end]):
                if overlap(self.cal[i], overlaps):
                    return False
                overlaps = self.cal[i]

        self.cal.append([start,end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
