class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums==None or nums==[]: return False
        
        i, end = 0, nums[0]
        while i<=end:
            if i==len(nums): return True
            end = max(end, i+nums[i])
            i+=1
        if end >= len(nums)-1:
            return True
        return False
#### O(n), O(1); 81, 7 Python3
