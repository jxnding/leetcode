class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(a, b, x, y):
            nonlocal strip
            # Base cases
            if b-a == 0 or y-x == 0:
                pass
            elif b-a == 1:
                for i in range(x, y):
                    strip.append(matrix[a][i])
            elif y-x == 1:
                for i in range(a, b):
                    strip.append(matrix[i][x])
            else:
                # Strip 4 sides and recurse
                # Top
                for i in range(x, y-1):
                    strip.append(matrix[a][i])
                # Right
                for i in range(a, b-1):
                    strip.append(matrix[i][y-1])
                # Bottom
                for i in range(y-1, x, -1):
                    strip.append(matrix[b-1][i])
                # Left
                for i in range(b-1, a, -1):
                    strip.append(matrix[i][x])
                # Recurse
                spiral(a+1,b-1,x+1,y-1)
        if matrix==[]: return []
        strip = []
        a, b, x, y = 0, len(matrix), 0, len(matrix[0])
        spiral(a, b, x, y)
        return strip
#### O(m*n), O(m*n); 87, 100 Python3
#### Tedious
# Way to zip: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
