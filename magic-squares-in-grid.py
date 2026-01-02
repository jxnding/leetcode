class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        # calculate all rows sums
        rows = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)-2)]
        # build across (the dimension thats not -2)
        for i in range(len(rows[0])):
            rows[0][i] = grid[0][i] + grid[1][i] + grid[2][i]
        # build down (efficiently)
        for i in range(1, len(rows)):
            for j in range(len(rows[0])):
                rows[i][j] = rows[i-1][j] - grid[i-1][j] + grid[i+2][j] 
        # --------------------------
        # Step 2: Calculate horizontal sums (your original "cols" variable)
        # cols[i][j] = sum of grid[i][j], grid[i][j+1], grid[i][j+2] (3-col horizontal row sum)
        # --------------------------
        cols = [[0 for _ in range(len(grid[0])-2)] for _ in range(len(grid))]
        # Build first column of horizontal sums (j=0)
        for i in range(len(cols)):
            cols[i][0] = grid[i][0] + grid[i][1] + grid[i][2]
        # Build remaining columns incrementally (fix your original missing logic)
        for j in range(1, len(cols[0])):
            for i in range(len(cols)):
                cols[i][j] = cols[i][j-1] - grid[i][j-1] + grid[i][j+2]  # fix: j-1 (remove left col) + j+2 (add new right col)

        # --------------------------
        # Step 3: Calculate main diagonal sums (\) for 3x3 subgrids
        # diag1[i][j] = sum of grid[i][j], grid[i+1][j+1], grid[i+2][j+2]
        # --------------------------
        diag1 = [[0 for _ in range(len(grid[0])-2)] for _ in range(len(grid)-2)]
        
        # 1. Seeds: Top row and Left column
        for j in range(len(diag1[0])):
            diag1[0][j] = grid[0][j] + grid[1][j+1] + grid[2][j+2]
        for i in range(1, len(diag1)):
            diag1[i][0] = grid[i][0] + grid[i+1][1] + grid[i+2][2]
            
        # 2. Slide: From (i-1, j-1) to (i, j)
        for i in range(1, len(diag1)):
            for j in range(1, len(diag1[0])):
                # Remove top-left element of old diagonal, add bottom-right of new
                diag1[i][j] = diag1[i-1][j-1] - grid[i-1][j-1] + grid[i+2][j+2]

        # --------------------------
        # Step 4: Calculate anti-diagonal sums (/) for 3x3 subgrids
        # diag2[i][j] = sum of grid[i][j+2], grid[i+1][j+1], grid[i+2][j]
        # --------------------------
        diag2 = [[0 for _ in range(len(grid[0])-2)] for _ in range(len(grid)-2)]
        
        # 1. Seeds: Top row and Right column
        for j in range(len(diag2[0])):
            diag2[0][j] = grid[0][j+2] + grid[1][j+1] + grid[2][j]
        for i in range(1, len(diag2)):
            # Seed the right-most possible anti-diagonal index
            last_col = len(diag2[0]) - 1
            diag2[i][last_col] = grid[i][last_col+2] + grid[i+1][last_col+1] + grid[i+2][last_col]
            
        # 2. Slide: From (i-1, j+1) to (i, j) - must iterate j backwards
        for i in range(1, len(diag2)):
            for j in range(len(diag2[0]) - 2, -1, -1):
                # Remove top-right of old diagonal, add bottom-left of new
                diag2[i][j] = diag2[i-1][j+1] - grid[i-1][j+3] + grid[i+2][j]

        ans = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                # Check all numbers are distinct 1-9
                nums = set()
                valid_nums = True
                for x in range(3):
                    for y in range(3):
                        num = grid[i-x][j-y]
                        if num < 1 or num > 9 or num in nums:
                            valid_nums = False
                            break
                        nums.add(num)
                    if not valid_nums:
                        break
                # Sums
                if (valid_nums and
                    rows[i-2][j-2] == rows[i-2][j-1] == rows[i-2][j] ==
                    cols[i-2][j-2] == cols[i-1][j-2] == cols[i][j-2] ==
                    diag1[i-2][j-2] == diag2[i-2][j-2]):
                    ans += 1
        return ans