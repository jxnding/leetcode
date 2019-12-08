currMin = prices[0]
ans = 0
for i in range(1,len(prices)):
    ans = max(ans, prices[i]-currMin)
    currMin = min(currMin, prices[i])
return ans
#### O(n), O(1); 76, 96 Python3
#### Faster!!!
#### Below on 11/16
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxA = [0]*len(prices)
        currMax = 0
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>currMax:
                currMax = prices[i]
            maxA[i]=currMax
        ans = 0
        for i in range(len(prices)-1):
            if maxA[i+1]-prices[i]>ans:
                ans = maxA[i+1]-prices[i]
        return ans