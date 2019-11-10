class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = {}
        for n in nums:
            if n in t:
                t[n]+=1
            else:
                t[n]=1
        o = []
        for key, value in t.items():
            if value>len(nums)//3:
                o.append(key)
        return o