class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Don't we just loop through the back and track the max?
        # Ok slightly diff, we need to calc the total open penalty first

        # O(n) and O(1). Just 2 for loops

        closePenalty = sum([c == 'Y' for c in customers])

        # assume we are totally closed
        minPenalty = (closePenalty, -1) #use -1 to represent 0
        openPenalty = 0
        for i, c in enumerate(customers):
            match c:
                case 'Y':
                    closePenalty -= 1
                case 'N':
                    openPenalty += 1
            # strict <, to get the earliest one
            if closePenalty + openPenalty < minPenalty[0]:
                minPenalty = (closePenalty + openPenalty, i)
        
        return minPenalty[1] + 1 #bc we use -1 to represent 0
        # closed_penalty = customers.count('Y')  # Still O(n), but more idiomatic than sum, sum([c == 'Y' for c in customers])
"""
3. Refinements (Staff SWE Level Polishing)
While your solution is correct, here are tweaks to make it more concise, efficient, and idiomatic (aligning with industry best practices):
A. Combine Initial Sum into the Single Pass
Your current code does two passes (one for sum([c == 'Y'...]), one for the loop). You can eliminate the first pass by precomputing the total Ys in the same loop, or by calculating the initial closed penalty as you go. Here’s how:
    ZX: ehhh not true
B. Remove Match/Case (for Compatibility)
match/case is Python 3.10+ syntax—while modern, some codebases still avoid it for backward compatibility. Replace with a simple if/else for broader support:
python
运行

# Replace:
match c:
    case 'Y':
        closePenalty -= 1
    case 'N':
        openPenalty += 1

# With:
if c == 'Y':
    closePenalty -= 1
else:
    openPenalty += 1

C. Variable Naming (Readability)
Use more descriptive variable names (e.g., min_penalty instead of minPenalty, best_hour instead of minPenalty[1])—this improves maintainability (critical for team environments).
D. Avoid Tuple for State Tracking
Storing (penalty, hour) in a tuple is functional but less readable than separate variables for min_penalty and best_hour.
"""