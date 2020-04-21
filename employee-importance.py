class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Turn to dict (faster)
        employee = {}
        for e in employees:
            employee[e.id] = (e.importance, e.subordinates)
        # Do it
        importance = 0
        queue = [id]
        while queue:
            curr = queue.pop()
            imp, sub = employee[curr]
            
            importance += imp
            queue += sub
        return importance
#### O(n), O(n); 91, 8 Python3
# https://leetcode.com/problems/employee-importance/discuss/112611/3-liner-Python-Solution-(beats-99)
# CONCISE