class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            i = (l+r)//2
            if nums[i]==target:
                return i
            elif nums[i]>target:
                r = i-1
            else:
                l = i+1
        return i if nums[i]>target else i+1
#### O(log n), O(1); 65, 84
#### TODO: Duplicates and why we return l (don't need my if statement)
# https://leetcode.com/problems/search-insert-position/discuss/15101/C%2B%2B-O(logn)-Binary-Search-that-handles-duplicate