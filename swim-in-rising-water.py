from queue import PriorityQueue

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def expandFrontier(curr):
            curr = curr[1]
            x, y = curr[0], curr[1]
            
            directions = []
            if x+1 < len(grid):
                directions.append((x+1,y))
            if y+1 < len(grid[0]):
                directions.append((x,y+1))
            if x-1 >= 0:
                directions.append((x-1,y))
            if y-1 >= 0:
                directions.append((x,y-1))
            
            for x, y in directions:
                if grid[x][y] != -1: 
                    frontier.put((grid[x][y],(x,y)))
                    grid[x][y] = -1

        
        if len(grid)<2: return grid[0][0]
        
        #pool, frontier
        #add neighbors to frontier when moving frontier to pool
        
        start = grid[0][0]
        target = grid[-1][-1]
        
        pool = set()
        pool.add(start)
        grid[0][0] = -1 #mark it
        frontier = PriorityQueue()
        frontier.put((grid[0][1],(0,1)))
        grid[0][1] = -1
        frontier.put((grid[1][0],(1,0)))
        grid[1][0] = -1
    
        t = start #in case start is not 0
        while True:
            # expand our pool from frontier
            while not frontier.empty():
                curr = frontier.get()
                if curr[0] <= t:
                    pool.add(curr[0])#add only value
                    expandFrontier(curr)
                else:
                    frontier.put(curr)
                    break
            
            if target in pool:
                return t
            
            t += 1