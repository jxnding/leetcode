
func numOfSubarrays(arr []int) int {
    // Contiguous so we can't sort
    // O(n^2) subarrays
    // thinking n^2 runtime, bc we need to try all subarrays, need to be efficient in calculating (reuse prev work)
    // space? n^2 is worst case, can we optimize? 

    // wait... are there any tricks? bitwise? we know +even means same parity, +odd means diff parity
        // we can reduce down to 0/1 binary array

    // 1,0,1 -> 2
    // 1,0,0,1 -> 3 

    // I think it's DP
        // start with first value, either odd or even
        // look at next, (currOdd = current sum)
            // if odd & currOdd: !currOdd;
    
    //// Naive Approach:
    sum := func(start, end int) int {
        total := 0
        for i := start; i < end; i++ {
            total += arr[i]
        }
        return total
    }

    total := 0
    for i := 0; i < len(arr); i++ {
        for j := i+1; j <= len(arr); j++ {
            // [i, j)
            if sum(i, j) % 2 == 1 {total += 1}
        }
    }
    return total
}
