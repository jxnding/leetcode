#### 2/15
class Solution:
    def search(self, nums, target: int) -> bool:
        def adjust(n):
            return (n+pivot)%len(nums)
        # Edge cases
        if nums==None or nums==[]: return -1
        if len(nums)==1:
            if nums[0]==target: return 0
            else: return -1
        # Find pivot
        valid = [0, len(nums)-1]
        while valid[1]-valid[0] > 1:
            a, b = valid[0], valid[0] + (valid[1]-valid[0]+1)//2
            if nums[a]<nums[b]: # Pivot after b (or NONE)
                valid = [b, valid[1]]
            elif nums[a]>nums[b]: # Pivot [a,b]
                valid = [a, b]
        pivot = valid[1] if nums[valid[1]-1]>nums[valid[1]] else 0
        print(pivot)
        # Find target (binary search)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r-l)//2+l
            print(adjust(mid))
            if nums[adjust(mid)]==target: return adjust(mid)
            elif nums[adjust(mid)]<target: l = mid+1
            else: r = mid-1
        return -1
#### O(log n), O(1); 88, 100 Python3; 39, 46 Python2
#### GOT IT!
#### TODO Didn't realize that pivot = smallest value

#### 1/25 Below. Nonworking
# import math
# class Solution:
#     def search(self, nums, target: int) -> int:
#         def points(f, s):
#             if f==s: return f, s
#             elif f<s: 
#                 f, s = (f+s)//3, math.ceil(2*(f+s)/3)
#             else:
#                 f = -(len(nums)-f)
#                 a, b = (f+s)//3, math.ceil(2*(f+s)/3)
#                 f, s = min(a,b),max(a,b)
#             f, s = regularize(f), regularize(s)
#             if nums[f]>nums[s]: return s, f
#             return f, s
#         def regularize(n):
#             if n<0: return n+len(nums)
#             if n>=len(nums): return n-len(nums)
#             return n
#         def rangeSize(f, s):
#             if f>s:
#                 return s+(len(nums)-f)
#             return s-f+1
#         # def merge(pf,ps,f,s):

            
#         f, s = 0, len(nums)-1
#         while True:
#             print()
#             print("%d, %d"%(f, s))
#             small, large = points(f, s)
#             pf, ps = f, s
#             print("%d, %d"%(small, large))
#             print("%d, %d"%(nums[small], nums[large]))
#             if nums[small]==target: return small
#             if nums[large]==target: return large
#             # if adjacent(small,large): return -1

#             if target>nums[small]:
#                 if target>nums[large]: f, s = large+1, small-1
#                 else: f, s = small+1, large-1
#             elif target<nums[small]:
#                 if target<nums[large]: f, s = large+1, small-1
#                 else: print("No") #f, s = large, small TODO
#             f, s = regularize(f), regularize(s)
#             if rangeSize(f,s)>=rangeSize(pf,ps): return -1
#         return -1

# # if nums==None: return -1
# # if len(nums)==0: return -1
# # if len(nums)==1:
# #     if nums[0]==target: return 0
# # return -1

# a = [4,5,6,7,0,1,2]
# # a = [1,3,5]
# print(Solution().search(a, 1))