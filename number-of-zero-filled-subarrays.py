class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        in_zero = False
        for i, n in enumerate(nums):
            if in_zero:
                if n!=0:
                    length = i-start
                    ans += length * length / 2 + length / 2
                    in_zero = False
            else:
                if n==0: 
                    start = i
                    in_zero = True
        if in_zero:
            length = len(nums)-start
            ans += length * length / 2 + length / 2
        return int(ans)