class Solution:
    # Bad solution
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = {}
        while nums:
            n = nums[0]
            del nums[0]
            if n in s:
                s[n] += 1
            else:
                s[n] = 1
                
        ans = []
        for k, v in s.items():
            if v == 1:
                ans.append(k)
        return ans
