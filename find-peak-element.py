class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)<=1: return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        if nums[0]>nums[1]: return 0
        i = 1
        while i<len(nums)-1:
            if nums[i-1]<nums[i]>nums[i+1]: return i
            elif nums[i+1]<nums[i]: i+=2
            else: i+=1
        return 0
#### O(n), O(1); 67, 100 Python3; 97, 30 Python2
#### TODO, Binary search...