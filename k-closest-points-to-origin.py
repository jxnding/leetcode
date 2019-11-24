import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x:math.sqrt(x[0]**2+x[1]**2))
        
        return points[:K]
#### 2 clap
#### O(n log n) and O(1)
#### Woah, the optimal solution is O(n)!