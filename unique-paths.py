class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial as f
        return f(m+n-2)//f(m-1)//f(n-1)
#### O(n), O(1); 91, 100 Python3
#### REVIEW: Runtime of factorial?
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [1 for _ in range(m)]
        for _ in range(1,n):
            for i in range(1,m):
                paths[i] += paths[i-1]
        return paths[m-1]
#### O(n^2), O(n); 91, 100 Python3
#### I did space-optimized DP!