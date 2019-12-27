class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # d = [{} for _ in range(n)]
        d = 10000000
        
        from queue import Queue
        q = Queue()
        q.put( (src, 0, 0) )
        while not q.empty():
            curr, steps, dist = q.get()
            # store
            if curr==dst: d = min(d, dist)
            if steps>K: continue
            # find neighbors
            for e in flights:
                if e[0]==curr: #only edges from current
                    # if e[1] in d and K+1 not in d[e[1]]: #stop if we are visiting to much
                    q.put( (e[1], steps+1, dist+e[2]) )
        # minVal = -1
        # for step, dist in d[dst]:
        #     minVal = min(minVal, dist)
        if d==10000000: return -1
        return d