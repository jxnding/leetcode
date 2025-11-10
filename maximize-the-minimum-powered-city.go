func maxPower(stations []int, r int, k int) int64 {
    /* 
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
    */
    if r < len(stations) {
        return int64(sum(stations) + k)
    }

    power := calculatePower(stations, r)
    val, loc := findMin(power)
    for i := 0; i < k; i++ {
        newStationLoc 
    }
    
}

// ZXTODO: confirm this works via side effects
func addPower(power []int, loc int) {

}

// Assumes r < N
func calculatePower(stations []int, r int) []int {
    power = make([]int, len(stations))
    // calculate 1st city
    for i := 0; i <= r; i++ {
        power[0] += stations[i]
    }

    // calculate rest of cities
    for i := 1; i < len(stations); i ++ {
        right := 0
        if i+r < len(stations) { right = stations[i+r] }
        left := 0
        if i-r-1 >= 0 { left = stations[i-r-1] }
        power[i] = power[i-1] + right - left
    }
    
    return power
}

func sum(input []int) int64 {
    var ans int64
    for _, val := range input {
        ans += val
    }
    return ans
}

// findMin iterates over an integer slice and returns the smallest value and its index.
// It returns (0, -1) for an empty slice to indicate failure.
func findMin(slice []int) (int, int) {
	if len(slice) == 0 {
		return 0, -1 // Return a failure case for an empty slice
	}

	// Initialize with the maximum possible int value to ensure the first element is always smaller
	minValue := math.MaxInt
	minIndex := -1

	for i, v := range slice {
		if v < minValue {
			minValue = v
			minIndex = i
		}
	}

	return minValue, minIndex
}