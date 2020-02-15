class Solution:
    def search(self, nums, target: int) -> bool:
        def adjust(n):
            return (n+pivot)%len(nums)
        # Edge cases
        if nums==None or nums==[]: return False
        # return True if (len(nums)==1 and nums[0]==target) else False
        if len(nums)==1:
            if nums[0]==target: return True
            return False
        # Find pivot
        valid = [0, len(nums)-1]
        while valid[1]-valid[0] > 1:
            a, b = valid[0], valid[0] + (valid[1]-valid[0]+1)//2
            print("Valid: %d, %d; %d, %d"%(valid[0],valid[1],a,b))
            if nums[a]<nums[b]: # Pivot after b (or NONE)
                valid = [b, valid[1]]
            elif nums[a]>nums[b]: # Pivot [a,b]
                valid = [a, b]
            # else:
            #     if a>0:
            #         if nums[a-1]<nums[a] and nums[b+1]>nums[a]:
        
        pivot = valid[1] if nums[valid[1]-1]>nums[valid[1]] else 0
        print(pivot)
        # Find target (binary search)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r-l)//2+l
            print(adjust(mid))
            if nums[adjust(mid)]==target: return True
            elif nums[adjust(mid)]<target: l = mid+1
            else: r = mid-1
        return False
# nums=[2,5,6,0,0,1,2]
# target=0
nums=[4,5,6,7,0,1,2]
target=0
x=Solution()
print(x.search(nums,target))
