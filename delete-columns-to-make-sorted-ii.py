class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Overall aglo:
        # loop forward
        #   if desc (-1), delete
        #   if equal (0), continue
        #   if ascending (1), return
        def calcColumn(column):
            # return {1,0,-1}
            equal = False
            for i in range(1,len(strs)):
                prevChar = strs[i-1][column]
                currChar = strs[i][column]
                if prevChar > currChar:
                    return -1
                if prevChar == currChar:
                    equal = True
            if equal: return 0
            return 1
        
        ans = 0
        for column in range(len(strs[0])):
            columnOrder = calcColumn(column)
            match columnOrder:
                case -1:
                    ans += 1
                case 0:
                    continue # tbh we don't need this, no logic to skip
                    ## OOps i misunderstood, I thought equal doesn't count. It does
                    # return ans
                case 1:
                    return ans
        return ans
# Above on 12/20. Not so simple.

# CORRECT
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Approach: store a sorted array O(n). Loop through each col and (maybe) update the sorted array
        # NOTE: updating sorted array can be tricky for runtime
        # NOTE: the sorted array is actually just T/F, not {0...N}, because the relationship is LOCAL! Just have to be bigger than prevRow
        # loop forward thru cols
        #   if sorted_array is None: special case
        #   if sorted_array is Sorted: RETURN! DONE! (because u can finish after an equal)
        #   if desc (-1) AND IT MATTERS, delete
        #   if equal (0) AND IT MATTERS, continue
        #   if ascend (1), RETURN! DONE!

        rowSort = [-1 for _ in strs] # -1 is desc, 0 is equal, 1 is asc
        rowSort[0] = 1 # rowSort[i] = is i-1 vs i, so ignore the 1st index
        ans = 0
        # loop through columns
        for colIdx in range(len(strs[0])):
            # Need a new array because col might be deleted
            newRowSort = rowSort.copy() # TODO: optimize?
            # loop through rows 1...N
            for rowIdx in range(1, len(strs)):
                prevRowChar, currRowChar = strs[rowIdx-1][colIdx], strs[rowIdx][colIdx]
                # Asc
                if currRowChar > prevRowChar:
                    newRowSort[rowIdx] = 1
                # Equal
                elif currRowChar == prevRowChar:
                    # Does it matter?
                    if rowSort[rowIdx] != 1:
                        newRowSort[rowIdx] = 0
                # Desc
                elif currRowChar < prevRowChar:
                    # Does it matter? Only if row isn't already ASC
                    if rowSort[rowIdx] != 1:
                        ans += 1
                        break
            else:
                # assign newRowSort only if we didn't break (Desc that mattered)
                rowSort = newRowSort
        
            if rowSort.count(1) == len(rowSort):
                return ans # HEURISTIC: return early
        return ans

