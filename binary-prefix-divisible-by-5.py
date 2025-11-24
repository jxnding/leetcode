class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        When adding a new digit, we "promote" the number (multiply by base) and add new
        Ex: 5 (base10) to 50 to 55 is promote(5) + add(0 or 5)
        """
        ans = [False] * len(nums)
        num = 0
        for i, n in enumerate(nums):
            # promote and add
            num = num * 2
            num = num + n

            # check
            if num % 5 == 0:
                ans[i] = True
        
        return ans