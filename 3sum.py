class Solution:
    def threeSum(self, nums):
        if nums==None or nums==[]: return []
        index = set()
        index.add(nums[0])
        total = set()
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                complement = 0-nums[i]-nums[j]
                if complement in index: 
                    triplet = tuple(sorted([ complement, nums[j], nums[i] ]))
                    total.add(triplet)
            index.add(nums[i])
        return list(total)
#### O(n^2), O(n); 5, 99 Python3
#### Runtime optimal
x = [-1,0,1,2,-1,-4]
print(Solution().threeSum(x))
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         index = {nums[0]:0}
#         total = []
#         for i in range(1, len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 complement = 0-nums[i]-nums[j]
#                 if complement in index: total.append([ complement, nums[j], nums[i] ])
#             index[nums[i]] = i
#         return total