class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))]
        h = []
        heapq.heappush(h, (T[0], 0))
        for i in range(1,len(T)):
            while h and h[0][0]<T[i]: #warmer temp
                day, idx = heapq.heappop(h)
                ans[idx] = i-idx
            heapq.heappush(h, (T[i], i))
        return ans
#### O(n log n), O(n); 24, 63; Python3; 12, 7 Python2
#### TODO: O(n) optimal. Did not realize that the stack will be sorted