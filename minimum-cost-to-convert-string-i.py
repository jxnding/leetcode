from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def dijkstra(a: str, b: str) -> int:
            dists = {}
            pq = []
            heapq.heappush(pq, (0, a)) #currCost, currNode
            visited = set()
            while pq:
                currCost, currNode = heapq.heappop(pq)
                if currNode in visited: continue
                visited.add(currNode)

                for neighbor, edgeCost in graph[currNode].items():
                    candidateCost = currCost + edgeCost 
                    if neighbor not in dists:
                        dists[neighbor] = candidateCost
                        heapq.heappush(pq, (candidateCost, neighbor))
                    elif candidateCost < dists[neighbor]:
                        dists[neighbor] = candidateCost
                        heapq.heappush(pq, (candidateCost, neighbor))
            # update all shortest distances from a
            nonlocal shortestPairs
            for end, dist in dists.items():
                shortestPairs[a][end] = dist
            if b not in dists:
                return -1
            return dists[b]

        ## Graph
        # Build graph
        graph = defaultdict(dict) #dict: a -> b -> cost, dict(str: dict(str: int))
        for i in range(len(cost)):
            a, b, currCost = original[i], changed[i], cost[i]
            # add to graph
            graph[a][b] = min(graph[a].get(b, float('inf')), currCost) #bro this is fucking stupid, that's a stupid case to check

        ## Precomputing
        # Get all the paths (pairs) we need
        shortestPairs = defaultdict(dict)
        ans = 0
        for i in range(len(source)):
            a, b = source[i], target[i]
            if a == b: continue
            # Shortest Path
            if a in shortestPairs and b in shortestPairs[a]:
                ans += shortestPairs[a][b]
            else:
                currCost = dijkstra(a, b)
                if currCost == -1: return -1
                ans += currCost
        return ans