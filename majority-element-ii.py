import pdb
class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        c1, c2 = None, None #can be 0,1; cannot be 0,0
        ct1, ct2 = 0, 0
        length = 0
        for n in nums:
            length+=1
            if n==c1:
                ct1+=1
            elif n==c2:
                ct2+=1
            elif ct1==0:
                c1 = n
                ct1+=1
            elif ct2==0:
                c2 = n
                ct2+=1
            else:
                ct1-=1
                ct2-=1
        ans = []
        if nums.count(c1)>length//3:
            ans.append(c1)
        if nums.count(c2)>length//3:
            ans.append(c2)
        return ans
a = [2,2,1,3]
print(Solution().majorityElement(a))
#### O(n), O(1)
#### Ahhhh, takes 2 passes!

#### 1 clap, O(n), O(n)?
#### TODO: what is the space complexity?
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         t = {}
#         for n in nums:
#             if n in t:
#                 t[n]+=1
#             else:
#                 t[n]=1
#         o = []
#         for key, value in t.items():
#             if value>len(nums)//3:
#                 o.append(key)
#         return o