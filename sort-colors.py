class Solution:
    def sortColors(self, nums:[int]) -> None:
        j, k = 0, len(nums)-1
        i = 0
        while i<=k:
            if nums[i]==0: #swap 0
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            elif nums[i]==2: #swap 2
                nums[i], nums[k] = nums[k], nums[i]
                i-=1 #check current swap
                k-=1 #one less 2
            i+=1
x = [2,0,2,1,1,0]
Solution().sortColors(x)
print(x)
#### O(n) and O(1)
#### https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions

#### 1 clap! But 2 loops...
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         count = [0,0,0]
#         for num in nums:
#             count[num]+=1
#         for i in range(len(nums)):
#             if count[0]>0:
#                 number = 0
#                 count[0]-=1
#             elif count[1]>0:
#                 number = 1
#                 count[1]-=1
#             else:
#                 number = 2
#             nums[i] = number