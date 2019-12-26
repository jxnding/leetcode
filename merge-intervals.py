class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1: return intervals
        intervals.sort(key=lambda x:x[0])
        ans, c = [], intervals[0]
        for i in range(1,len(intervals)):
            n = intervals[i]
            if n[0]<=c[1]: #overlap
                c[1]=max(c[1],n[1])
            else:
                ans.append(c)
                c = n
        ans.append(c)
        return ans
#### O(n log n), O(1); 99, 6 Python3; 22, 7 Python2
