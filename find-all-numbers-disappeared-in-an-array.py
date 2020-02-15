class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def follow(n):
            nonlocal nums
            if n>len(nums): return
            curr = nums[n-1]
            if curr > 0: # actual number
                nums[n-1] = -1
                follow(curr)
            elif curr < 0: # already a counter
                nums[n-1] -= 1
            else:
                nums[n-1] = -1
        if nums==None or nums==[]: return []
        
        for i, val in enumerate(nums):
            if val > 0:
                n = val
                nums[i] = 0
                follow(n)
        
        ans = []
        for i, val in enumerate(nums):
            if val == 0: ans.append(i+1)
        return ans
#### O(n), O(1); 14, 46 Python3