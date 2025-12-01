class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        count = collections.Counter({0: 1})

        sum_ = 0

        ans = 0

        for n in nums:

            sum_ += n

            ans += count[sum_ - k]

            count[sum_] += 1

        return ans

^ Mar 14, 2024 22:40

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        How many arrays add up to k-nums[i]?
        Prefix? prefix represents how many are eligible up to the current index (because it's contiguous)
        prefix = {}
        for n in nums:
            # Do past first
            if k-n in prefix:
                ans += prefix[k-n]
                prefix[k-n+1] += prefix[k-n]
                prefix[k-n] = 0
            # Prep for future
            prefix[n] += 1

        Example:
        1,1,50,1,1 k=2

        BREAKTHROUGH! Use k-currSum instead of k-n
        HINT: currSum includes current index
        HINT: prefix needs to be init'd as {0: 1}
        HINT: currSum-k instead of k-currSum
        HINT: not ans += 1 but ans += prefix[currSum-k]
        prefix = {0: 1}
        currSum = 0
        for n in nums:
            currSum += n
            # Do past first
            if k-currSum in prefix:
                ans += 1
            # For the future
            prefix[currSum] += 1
        return ans
        27ms
        Beats83.37%
        Analyze Complexity
        Memory
        20.38MB
        Beats71.09%

        """
        prefix = {0: 1}
        currSum = 0
        ans = 0
        for n in nums:
            currSum += n
            # Do past first
            # if -(k-currSum) in prefix:
            ans += prefix.get(-(k-currSum), 0)
            # For the future
            prefix[currSum] = prefix.get(currSum, 0) + 1
        return ans
