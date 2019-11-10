class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        #Base cases
        ways[0] = 1
        #DP
        for i in coins:
            for a in range(i,amount+1):
                ways[a] += ways[a-i]
        
        return ways[amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [[0 for x in range(len(coins))] for x in range(amount+1)]
        #Base cases
        ways[1]=[1 for x in range(len(coins))]
        for a in range(1, amount+1):
            ways[a][0] = 1
            
        #DP
        for i in range(len(coins)):
            for a in range(1,amount+1):
                ways[a][i] = ways[a][i-1]+ways[a-coins[i]][i]
        
        return ways[amount][-1]