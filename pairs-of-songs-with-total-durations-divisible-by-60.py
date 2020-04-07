class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        comp = {}
        for i, t in enumerate(time):
            if i>0:
                ans += comp.get(60-(t%60), 0)
                ans += comp.get(-(t%60), 0) # for perfect multiples
            curr = comp.get(t%60, 0)
            comp[t%60] = curr + 1
        return ans
#### O(n), O(n); 9, 9 Python3
## REVIEW