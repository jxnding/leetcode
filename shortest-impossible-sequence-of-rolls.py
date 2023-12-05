class Node:
    def __init__(self, k):
        self.sequence = []
        self.candidates = [] #indices where valid sequences end
        self.leaves = [None for _ in range(k)]

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ## Setup
        root = Node(k)
        # add all candidates to root
        root.candidates = [x for x in range(len(rolls))]
        tree = [root]
        ## for s in sequences (1 ... n^k)
        length = 1
        while tree:
            root_node = tree.pop()
            # possible next rolls, looking for this
            for curr_next in range(1, k):
                next_node = Node(k)
                for c in root_node.candidates: # look in all candidates
                    # if c+1 == s+1 (next one)
                    if c<(len(rolls)-1) and rolls[c+1]==curr_next: # good sequence
                        next_node.candidates.append(c+1)
                # if no candidates, we're done
                if next_node.candidates == []: return length
                # Careful here, need to store the sequence info (do we?)
                root_node.leaves[curr_next] = next_node
                tree.append(next_node)
            length += 1

        # add all candidates to root
        # for s in sequences (1 ... n^k)
            # for c in root.candidates
                # if c+1 == s+1 (next one)
                # else (donezo!)
                    # return len(s)
        return 0

=================
class Node:
    def __init__(self, k):
        self.sequence = 0
        self.candidates = [] #indices where valid sequences end
        self.leaves = [[] for _ in range(k)]

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        def populate_leaves(root_node):
            nonlocal k
            nonlocal rolls
            candidates = root_node.candidates
            for c in candidates:
                if c<(len(rolls)-1):
                    root_node.leaves[rolls[c+1]-1].append(c+1)
            # return root_node
            # for curr_next in range(1, k):
            #     next_node = Node(k)
            #     next_node.sequence(root_node.sequence + [curr_next])
            #     for c in candidates:
            #         if c<(len(rolls)-1) and rolls[c+1]==curr_next: # good sequence
            #             next_node.candidates.append(c+1)
            
            #     if next_node.candidates == []: return len(next_node.sequence)
            # return None
        ## Setup
        root = Node(k)
        # add all candidates to root
        root.candidates = [x for x in range(len(rolls))]
        tree = [root]
        ## for s in sequences (1 ... n^k)
        while tree:
            root_node = tree.pop()
            populate_leaves(root_node)
            for l in range(len(root_node.leaves)):
                print(root_node.leaves[l])
            for next_roll in root_node.leaves:
                if next_roll == []: 
                    return root_node.sequence + 1
                else:
                    next_node = Node(k)
                    next_node.sequence = root_node.sequence + 1
                    next_node.candidates = next_roll
                    tree.append(next_node)
            # possible next rolls, looking for this
            # for curr_next in range(1, k):
            #     next_node = Node(k)
            #     for c in root_node.candidates: # look in all candidates
            #         # if c+1 == s+1 (next one)
            #         if c<(len(rolls)-1) and rolls[c+1]==curr_next: # good sequence
            #             next_node.candidates.append(c+1)
            #     # if no candidates, we're done
            #     if next_node.candidates == []: return length
            #     # Careful here, need to store the sequence info (do we?)
            #     root_node.leaves[curr_next] = next_node
            #     tree.append(next_node)
            # length += 1

        # add all candidates to root
        # for s in sequences (1 ... n^k)
            # for c in root.candidates
                # if c+1 == s+1 (next one)
                # else (donezo!)
                    # return len(s)
        return len(rolls)