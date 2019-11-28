class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,e in enumerate(nums):
            ind1 = -1
            ind2 = -1
            try:
                ind1 = d[target-e]
                ind2 = i
                return ind1,ind2
            except:
                d[e]=i
            
