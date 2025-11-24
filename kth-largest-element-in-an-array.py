class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums, k)
        pivotIdx = len(nums)//2

        larger = []
        smaller = []
        # sameCount = 0
        for n in nums:
            if n > nums[pivotIdx]:
                larger.append(n)
            if n < nums[pivotIdx]:
                smaller.append(n)
            # else:
            #     sameCount += 1
        numEquals = len(nums)-len(smaller)-len(larger)
        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif len(larger) + numEquals >= k:
            return nums[pivotIdx]
        else:
            return self.findKthLargest(smaller, k-len(larger)-numEquals) # k-len(smaller) = len(larger) + sames 