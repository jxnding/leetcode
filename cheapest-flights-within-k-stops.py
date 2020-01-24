class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        d = 10000000
        # edges = {}
        edges = collections.defaultdict(dict)
        for a,b,c in flights:
            edges[a][b]=c
        
        from queue import Queue
        q = Queue()
        q.put( (src, 0, 0) )
        while not q.empty():
            curr, steps, dist = q.get()
            # store
            if curr==dst: d = min(d, dist)
            if steps>K: continue
            # find neighbors
            for b, c in edges[curr].items():
                q.put( (b, steps+1, dist+c) )
        if d==10000000: return -1
        return d