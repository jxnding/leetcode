class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def explore(start_node: int):
            # nonlocal res_nodes
            # nonlocal edge_list
            ans = 1
            for n in edge_list[start_node]:
                if n in res_nodes: continue
                ans += explore(n)
            return ans
        res_nodes = set(restricted)
        edge_list = [[] for _ in range(n)]
        for a, b in edges: 
            edge_list[min(a, b)].append(max(a, b))
        print(edge_list)
        return explore(0)
#TODO: Not done.