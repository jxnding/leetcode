class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[1]-x[0]) #sort, n log n
        a, b = 0, 0 #counters for the cities
        i, j = 0, len(costs)-1
        cost = 0
        while a<len(costs)/2 and b<len(costs)/2: #loop until we hit the N people constraint
            if abs(costs[i][1]-costs[i][0])>abs(costs[j][1]-costs[j][0]):
                currCost = costs[i]
                i+=1
            else:
                currCost = costs[j]
                j-=1
            
            if currCost[0]<currCost[1]: #choose A
                a+=1
                cost+=currCost[0]
            else:
                b+=1
                cost+=currCost[1]
        #A and B won't both == N
        if a==len(costs)/2: #everyone to B
            while j!=i:
                cost+=costs[j][1]
                j-=1
            cost+=costs[j][1]
        else:
            while j!=i:
                cost+=costs[j][0]
                j-=1
            cost+=costs[j][0]
        return cost
#### 3 clap
#### O(n log n) and O(1)