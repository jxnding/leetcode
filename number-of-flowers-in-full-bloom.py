class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        #think of solution for 3m, then write brute force in 10m
        #never delete code, comment it
        #before you run, think of corner cases
        #you get multiple shots
        #MLE and TLE in this problem
        #sweep line algorithms
#         flowerClock = {}
#         for f in flowers:
#             start, end = f
#             for i in range(start, end+1):
#                 if i in flowerClock:
#                     flowerClock[i] = flowerClock[i] + 1
#                 else:
#                     flowerClock[i] = 1
        
#         return [flowerClock.get(p, 0) for p in persons]
        #fill up the intervals
    
        #ants on a log problem
        superList = []
        for f in flowers:
            superList.append([f[0], 1])
            superList.append([f[1]+1, -1])
            
        for i, p in enumerate(persons):
            superList.append([p, 69, i])
        superList.sort()#bigdickvlad: python already knows
        
        # personsDict = {}
        # for i, p in enumerate(persons):
        #     personsDict[p] = [i]
        
        counter = 0
        answer = [0] * len(persons)
        for item in superList:
            t, e = item[0], item[1]
            if e==69:
                answer[item[2]] = counter
            else:
                counter += e
        return answer
        
        #f[1]+1
        #flower and person at the same time