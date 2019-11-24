class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def visit(index):
            nonlocal nums
            if index>=len(nums):
                return
            if nums[index]<1:
                nums[index]=-1
            else:
                temp = nums[index]
                nums[index]=-1
                visit(temp-1) #index from 1
        if nums==[]:
            return 1
        for i in range(len(nums)): #get rid of negatives
            if nums[i]<0:
                nums[i]=0
        for i, value in enumerate(nums):
            if value>0:
                if value<=i+1:
                    nums[i]=0
                    nums[value-1]=-1
                else:
                    nums[i]=0
                    visit(value-1)
        for i in range(len(nums)):
            if nums[i]==0:
                return i+1
        return len(nums)+1
#### O(n), O(1)
#### I should just pad 1 instead of all the +-1 index math