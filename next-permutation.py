class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reconstruct(a):
            nonlocal nums
            # find smallest
            min_ind = a+1
            for i in range(-1, a, -1):
                if nums[a]<nums[i]<nums[min_ind]: min_ind = i
            # Switch
            b = min_ind
            nums[b], nums[a] = nums[a], nums[b]
            extra = nums[a+1:]
            extra.sort()
            for i in range(len(extra)):
                nums[i+a+1] = extra[i]
        # Find reverse sorted
        reverse = -1
        i = -2
        while i > -len(nums)-1:
            if nums[i] >= nums[reverse]: reverse = i
            else:
                return reconstruct(i)
            i -= 1
        # Already max
        nums.sort()
#### O(n log n), O(1); 69, 100 Python3
#### O(1) only achived with in-place sorting
#### TODO: O(n) solution