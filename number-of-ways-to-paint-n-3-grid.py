class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        def valid():
            valid_comp = []
            for a in range(12):
                for b in range(12):
                    this_valid = True
                    for i in range(3):
                        if configs[a][i]==configs[b][i]: this_valid = False
                    if this_valid: valid_comp.append((a,b))
            return valid_comp
        # Configurations
        configs = [(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
        # Legal configs
        for i in range(len(configs)-1,-1,-1):
            if configs[i][0]==configs[i][1] or configs[i][1]==configs[i][2]: del configs[i]
        # Track ways
        old, new = [1]*12, [0]*12
        valid_comp = valid()
        for i in range(1, n): #Start at 1x3
            # Compare 12x12
            for j, k in valid_comp:
                new[k] = (new[k]+old[j])%mod
            old = new
            new = [0]*12
        return sum(old)%mod
#### O(n), O(1); 27, 100 Python3 by saving valid comparisons into a list
# 4/13 4:03 -> 4:38

class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        def valid(a, b):
            for i in range(3):
                if configs[a][i]==configs[b][i]: return False
            return True
        # Configurations
        configs = [(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
        # Legal configs
        for i in range(len(configs)-1,-1,-1):
            if configs[i][0]==configs[i][1] or configs[i][1]==configs[i][2]: del configs[i]
        # Track ways
        old, new = [1]*12, [0]*12
        for i in range(1, n): #Start at 1x3
            # Compare 12x12
            for j in range(len(old)):
                for k in range(len(new)):
                    if valid(j, k):
                        new[k] += old[j]
            old = new
            new = [0]*12
        return sum(old)%mod
#### O(n), O(1); 7, 100 Python3