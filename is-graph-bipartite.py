class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def BFS(currNode):
            nonlocal bipartite
            if currNode in visited: return
            neighbors = graph[currNode]
            currPartition = assigned[currNode]

            for n in neighbors:
                if n in assigned:
                    if assigned[n] == currPartition: 
                        bipartite = False
                else: #not assigned yet
                    assigned[n] = not currPartition
            visited[currNode] = True
            
            for n in neighbors: BFS(n)

        
        # dict to store partitions: O(V) storage
        visited = {}
        assigned = {}
        bipartite = True
        
        # BFS, each frontier must be opposite the previous
        for i in range(len(graph)):
            if i not in visited: #in case there are unconnected nodes
                assigned[i] = True
                BFS(i)
                
        return bipartite

