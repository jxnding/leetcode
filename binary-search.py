class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            i = (l+r)//2 #middle of the range
            if nums[i]==target:
                return i
            elif nums[i]>target:
                r=i-1
            else:
                l=i+1
        return -1
#### Why doesn't my recursive solution (below) work?
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import math
        def find(i, r):
            if r==0:
                return -1
            nonlocal nums
            nonlocal target
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return find(i-r, math.ceil(r/2))
            else:
                return find(i+r, math.ceil(r/2))
        return find(len(nums)//2, math.ceil(len(nums)/4))