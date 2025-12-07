class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        """
        Runtime
        0ms
        Beats100.00%
        Memory
        17.71MB
        Beats68.09%
        """
        leftSum, rightSum = 0, sum(nums)
        ans = 0
        for i, n in enumerate(nums):
            if i == len(nums) - 1: break
            leftSum += n
            rightSum -= n
            if (leftSum - rightSum) % 2 == 0:
                ans += 1
        return ans