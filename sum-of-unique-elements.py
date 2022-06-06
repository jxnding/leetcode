class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
                
        ans = 0
        for k, v in d.items():
            if v == 1: ans += k
        return ans