from functools import cache
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        ## Observations
        # The sum is always the same, regardless of how you break down the subsets
        #   sum = sum(list) / k
        #   if it's not divisble, then there's no answer
        #   if it's divislbe, may be an answer ([1000,1,1,1], k=4 has no answer)
        # We can only add 1 item at a time in the DP loop, so there's an alternating pattern of YES/NO
        #    (you need to have NO solution to have a solution, and need to have a solution to have NO solution on the next iteration)
        #    except in the case of 4x3, 3x4
        # Can we try to not store the actual partitions? 

        ## DP, what are we storing?
        # yes/no
        # sum

        ## DP conditions:
        # if DP[list - 1][k - 1] == list[-1]: true, list[-1]  # we can make a new set of {list[-1]}
        # if # we add the new item to the current min subset && only 1 min_subset && all other subsets are equal && other_subsets - min_subset = list[-1]
        #   ^this condition is too hard, use backtracking for this

        ## try nums = [1,2,3,4], k = 3
        ## part(list, k, target)
        # partition([1], 1) = yes,1
        # partition([1,2], 1) = yes,3
        # partition([1,2], 2) = no
        # partition([1,2,3], 2) = yes,3 (part([1,2], 1) = 3)
        # partition([1,2,3], 3) = no (part([1,2], 2) = no) ???
        # partition([1,2,3,4], 2) = yes (part([1,2,3,4], 1) = no) ??? assume we have this solver (k=2)
        ## yes bc part([1,4], 1) == part([2,3], 1)
        ## part([1,2,3], 1, target=)
        # part([1,2,3,4], 3) = no

        ### Backtracking
        ## I want to preserve order of list
        # Bc each item MUST belong to a subset, no difference between backtrack([1,2,3], 1) and backtrack([2,3,4], 1)
        # for loop, across how much of the list is consumed by 1 subset. backtrack([1,2,3], 2, t=3)
        #      backtrack([1,2], 1, t=3)
        #      backtrack([1], 1, t=3)
        # for loop, backtrack([1,2,3,4], 2, t=5)
        #      backtrack([1,2,3], 1, t=5)

        ## Algo
        # if remaining_set == []:
        #       if k == 0: return YES
        #       else: return NO
        # if curr_set == target
        #       backtrack(remaining_set, k-1, target)
        # if curr_set < target
        #       if curr_item is small enough, take it
        #       else go to next item

        #### Submission notes
        # TLE if I don't @cache & use tuple
        # beats 18% if I @cache (though the conversion from list->tuple is an extra O(n) in deepcopy_remove)

        def deepcopy_remove(curr_set, remove_i):
            new_set = [x for i, x in enumerate(curr_set) if i != remove_i]
            # print(new_set)
            new_set = tuple(new_set)
            return new_set
        # ZXTODO: target & curr_sum can be combined into 1 arg
        @cache
        def backtrack(remaining_set, k, target, curr_sum):
            # print(f"{remaining_set=}, {k=}, {target=}, {curr_sum=}")
            nonlocal ans
            if ans == True: return True # break ZXTODO
            if curr_sum == target:
                backtrack(remaining_set, k-1, target, 0) # k-1 because we satisfied a subset
            if len(remaining_set) == 0:
                if k == 0: 
                    ans = True
                    return True # ZXTODO: what about the return values?
                else: return False
            if curr_sum < target:
                for i, n in enumerate(remaining_set):
                    if n <= target - curr_sum:
                        # ZXNOTE: Can we remove and append? Will this mess up the order of the list? Does it matter?
                        # ZXTODO: remaining_set.remove(i); backtrack; remaining_set.append(n)
                        backtrack(deepcopy_remove(remaining_set, i), k, target, curr_sum + n) # curr_sum - n, bc we took an item
        if sum(nums) % k != 0: return False
        ans = False
        nums = tuple(nums)
        backtrack(nums, k, sum(nums)//k, 0)
        return ans