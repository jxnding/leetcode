class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Guard against 1 because we assume 2 (lookahead of 1)
        if nums and len(nums)==1: return 1
        delete, index = 0, 0
        N = len(nums)
        #-1 because we lookahead 1
        while (delete + index < N-1):
            curr = nums[index]
            lookahead = nums[index+1]
            if lookahead == curr:
                del nums[index+1]
                delete += 1
            else:
                index += 1
        return N-delete
# Good! Done quick, like 5 min, and actually sniped it on the first try. Was a good confidence boost after getting nuked by 2 leetcode mediums for 2 weeks straight (max product of subarray; minimum steps to make array equal)