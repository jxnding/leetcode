from queue import PriorityQueue
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        """ 
        Calculate power[i]:
        brute force loop is O(n * r)
        can optimize: in the middle (no edge logic), when we move to the next city, we can just add the next station and remove the previous station
        i.e. power[i] = power[i-1] + stations[i+r] - stations[i-r-1]
        optimized is O(n + r)
        
        Where to add?
        Add to within range of the min city, heuristics
                Hit multiple min cities, max "value" per station
                        I think we need priorityQueue. Get min, then keep getting until another city in range.
                Be as middle as possile, again max "value"

        Is greedy OK?
                Will we have situations where given k=2, we will place 1 differently than k=1
                I think greedy is ok... but no proof

        If R >= N (len of stations), then the problem is very easy
                Just keep adding. Ans = sum(stations) + k

        Oh shit: hard example
        r = 1
        9,1,9,0,9,9,9,1,9,0
        """
        if r >= len(stations):
            return sum(stations) + k

        power = self.calculatePower(stations, r)
        # val, loc = self.findMin(power)

        for i in range(k):
            # # initalize priorityqueue, use index for stability
            pq = PriorityQueue()
            for i, val in enumerate(power):
                pq.put((val, i, i)) # Sort by val, sort by index, item (index)
            (currVal, currLoc, _) = pq.get()

            # where to add power?
            # find next closest city, if possible
            secondVal, secondLoc = None, 10000000000000000000
            while abs(secondLoc - currLoc) > 2 * r and pq.qsize() > 0:
                (secondVal, secondLoc, _) = pq.get()

            # no 2nd city found, use Heuristic #2
            if secondVal == None:
                addLoc = self.heuristicTwo(power, r, currLoc)
            else:
                # try leftmost that includes both
                rightLoc = max(secondLoc, currLoc)
                leftmostLoc = max(r, rightLoc)
                addLoc = leftmostLoc
            self.addPower(power, r, addLoc)

        return min(power)


    # returns the middlest eligible location
    def heuristicTwo(self, power, r, currLoc) -> int:
        # mid = len(power)
        # TODO
        return min(currLoc + r, len(power)-1)


    # ZXTODO: confirm this works via side effects
    def addPower(self, power: List[int], r: int, loc: int):
        start = max(0, loc - r)
        end = min(loc + r, len(power)-1)

        for i in range(start, end + 1):
            power[i] += 1

    # Assumes r < N
    def calculatePower(self, stations: List[int], r: int) -> List[int]:
        n = len(stations)
        power = [0] * n
        
        # calculate 1st city
        for i in range(r + 1):
            power[0] += stations[i]

        # calculate rest of cities
        for i in range(1, n):
            right = 0
            if i + r < n:
                right = stations[i + r]
            left = 0
            if i - r - 1 >= 0:
                left = stations[i - r - 1]
            power[i] = power[i - 1] + right - left
        
        return power

    # findMin iterates over an integer slice and returns the smallest value and its index.
    # It returns (0, -1) for an empty slice to indicate failure.
    def findMin(self, slice_in: List[int]) -> (int, int):
        if not slice_in:
            return 0, -1 # Return a failure case for an empty slice

        # Initialize with the maximum possible int value to ensure the first element is always smaller
        min_value = sys.maxsize
        min_index = -1

        for i, v in enumerate(slice_in):
            if v < min_value:
                min_value = v
                min_index = i

        return min_value, min_index