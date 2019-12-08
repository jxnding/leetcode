class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]: return 0
        # First transaction
        profit1 = [0 for _ in range(len(prices))]
        currMin = prices[0]
        for i in range(1, len(prices)):
            profit1[i]=max(profit1[i-1],prices[i]-currMin)
            currMin = min(currMin,prices[i])
        # Second transaction
        profit2 = [0 for _ in range(len(prices))]
        currMax = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            profit2[i]=max(profit2[i+1],currMax-prices[i])
            currMax = max(currMax,prices[i])
        # Max
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, profit1[i]+profit2[i])
        return ans
#### O(n), O(n); 74; 100 Python3; 55, 36 Python2
#### Could optimize away profit2
#### TODO: Actually there is O(1) space solution below
class Solution(object):
    def maxProfit(self, prices):
        if prices==[]: return 0
        buy1, buy2 = -prices[0],-prices[0]
        sell1, sell2 = 0, 0
        for p in prices:
            sell2 = max(sell2, buy2+p)
            buy2 = max(buy2, sell1-p)
            sell1 = max(sell1, buy1+p)
            buy1 = max(buy1, -p)
        return sell2
#### 74, 81 Python2