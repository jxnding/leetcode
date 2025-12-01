class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        Simulation approach (but this loops through minutes, could be very long)
        There's no reason to not swap ASAP, every minute
        Sort batteries, pull from the biggest ones (need to preserve the widest front)
            Since decrement is fixed at -1, we should be able to avoid sorting again
            Continue until front < computers (aka too many 0-batteries, dead batteries)

        How many watt-hour can be wasted?
        """

        batteries.sort(reverse=True) # Desc
        ans = 0
        while True:
            if len(batteries) < n:
                return ans
            if len(batteries) == n:
                return ans + min(batteries)
            # Heuristic, we want to take the jut of the front, or 1 if jut is 0
            minutesRun = max(1, batteries[n-1] - batteries[n])
            for i in range(n):
                batteries[i] -= minutesRun
            ans += minutesRun

            for i in range(n-1,-1,-1):
                if batteries[i] == 0:
                    del batteries[i]
            batteries.sort(reverse=True)
        return ans

