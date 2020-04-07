class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def push(target):
            nonlocal nums
            if nums[target] == None:
                nums[target] = str(target)+'a'
            elif type(nums[target]) == str:
                if nums[target]=='b':
                    pass #more than 2
                elif nums[target][-1]=='a':
                    nums[target]='b'
            else:
                temp = nums[target]
                nums[target] = str(target)+'a'
                push(temp)
        i = 0
        while i<len(nums):
            if nums[i] == None:
                pass
            elif type(nums[i]) == str:
                pass
            else:
                temp = nums[i]
                nums[i] = None
                push(temp)
            i += 1
        for n in nums:
            if type(n)==str and n[0]!='b': return int(n[:-1])

#### TODO
#### Maybe O(n), O(1) if input range is between 0 and len. But really bad solution