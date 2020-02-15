class Solution:
    def checkRecord(self, s: str) -> bool:
        late, absent = 0, 0
        for c in s:
            if c=='L':
                late+=1
                if late==3: return False
            elif c=='A':
                absent+=1
                if absent>1: return False
                late = 0
            else:
                late = 0
        return True

#### O(n), O(1); 64, 100 Python3
