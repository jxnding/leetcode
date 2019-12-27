class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
#### 96, 6 Python3
#### TODO Proof
# Below 11/10
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0,len(nums),2):
            total+=nums[i]
        return total