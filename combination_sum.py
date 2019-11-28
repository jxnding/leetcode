#5/30/19
#### Interview for Mathworks
#Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

#The same repeated number may be chosen from candidates unlimited number of times.
import pdb
def combinationSum(candidates, target):
    comb = [0]*(target+1)
    # how many combinations for i?
    for i in range(1,target+1):
        icombs = 0

        # i itself is in cand
        for n in candidates:
            if n == i:
                icombs+=1

        # loop from 1 to i/2
        trigger = False
        for j in range(1,int(i/2)+1):
            if (i-j) in candidates:
                trigger = True
                icombs+=comb[j]
        if i==4:
            pdb.set_trace()
        comb[i]=icombs
    pdb.set_trace()
    return comb[target]
combinationSum([2,3,6,7],7)
