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

#### Wrong solution
## My intuition was totally wrong. Rip.
# there's not that many degrees of freedom
# I see so is the core logic here basically this That when I'm on like the third script of each row I look at the left. I look at the top. But I can't just ask. Okay. My the number of ways I can end in red here is the number of ways I ended non red at the top. Plus number of ways I ended non red from the left because those ways are connected by the top left. Diagonal grid so they're actually having a relationship. limitation that I'm not mapping Is that correct? And if that's correct is my current solution over or underestimating the total. answer 
class Solution:
    def numOfWays(self, n: int) -> int:
        ## Base case
        # For 1 square: 1 way to end in red, 1 way to end in yellow, 1 way to end in green
        ## DP condition
        # do the 3 colors separately
        # ex: current square ending at green = # of ways Top square ends in Red or Yellow + # of ways Left square ends in Red or Yellow
        ## Return the 3 colors summed up

        # dp = [(0,0,0), (0,0,0), (0,0,0)]
        # dp = [(1,1,1), (1,1,1), (1,1,1)]
        dp = [None, None, None]
        for i in range(n):
            for j in range(3):
                curr = Triple(0,0,0)
                if i == 0 and j == 0:
                    curr = Triple(1,1,1)
                if i > 0:
                    curr = curr + dp[j] #top, dp[j] not overwritten yet
                if j > 0:
                    curr = curr + dp[j-1] #left, dp[j-1] updated already
                dp[j] = curr
        return dp[-1].totalWays() % (10**9 + 7)

class Triple:
    def __init__(self, x, y, z):
        self.red = x
        self.yellow = y
        self.green = z

    def __add__(self, other):
        return Triple(self.red + other.yellow + other.green,
                    self.yellow + other.red + other.green,
                    self.green + other.red + other.yellow
                    )

    def totalWays(self):
        return self.red + self.yellow + self.green