class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        I think this has to be backtracking. Because it's too tricky with things like "pen" vs "penis". 
        You don't know what to take with a greedy approach.

        Is it like trying to navigate a trie and trying all possible paths?
        We keep going, then when we get to a leaf, we go back to the root.
        The only divergence is when 1 word is a prefix of another (and you go back to the root early)

        for i in range(len(s)):
            if branch (diverge):
                return wordBreak(root, i+1) or wordBreak(node, i+1)
            elif s[i] in trie.map:
                return wordBreak(node, i+1)
            else:
                return False
        """
        # def wbAlgo(trieNode, index):
        #     if index == len(s):
        #         return trieNode.terminal # done, consumed the whole string, are we at the end of a word?
        #     nonlocal trieRoot
        #     currChar = s[index]
        #     # print(f'index: {index} char:{currChar}')
        #     # print(f'trieNode.map{trieNode.map} trieNode.terminal{trieNode.terminal}')
        #     if trieNode.terminal:
        #         if currChar in trieRoot.map and currChar in trieNode.map:
        #             return wbAlgo(trieRoot.map[currChar], index+1) or wbAlgo(trieNode.map[currChar], index+1)
        #         elif currChar in trieRoot.map:
        #             return wbAlgo(trieRoot.map[currChar], index+1)
        #         elif currChar in trieNode.map:
        #             return wbAlgo(trieNode.map[currChar], index+1)
        #         else:
        #             return False #TODO: what's this mean?
        #     elif currChar in trieNode.map:
        #         return wbAlgo(trieNode.map[currChar], index+1)
        #     else:
        #         return False
        #     # if currChar in trieNode.map and trieNode.terminal:
        #     #     return wbAlgo(trieRoot, index+1) or wbAlgo(trieNode.map[currChar], index+1)
        #     # elif currChar in trieNode.map:
        #     #     return wbAlgo(trieNode.map[currChar], index+1)
        #     # elif trieNode.terminal:
        #     #     return wbAlgo(trieRoot, index+1)
        #     # else:
        #     #     return False

        # # Build trie
        # trieRoot = Trie()
        # for word in wordDict:
        #     trieRoot.add(word, 0)
        
        # # Word break algo
        # return wbAlgo(trieRoot, 0)

        """
        Approach 2 by neetcode, go backwards, DP, try every word
        DP[len(s)] = True
        for i in reverse:
            for w in words:
                if in_bounds && chars_match && DP[i+len(w)]:
                    DP[i] = True
        return DP[0]
        """

        DP = [False for _ in s]
        DP.append(True)
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # choose order carefully, and most expensive operation at the end
                if i+len(w)<=len(s) and DP[i+len(w)] and w==s[i:i+len(w)]:
                    DP[i] = True
                    break #1 true is good enough
        return DP[0]
            


# class Trie:
#     def __init__(self):
#         self.map = {}
#         self.terminal = False

#     def add(self, word, index):
#         if index == len(word):
#             self.terminal = True # TODO: check
#             # print("TERMINAL")
#             return
#         char = word[index]
#         if char in self.map:
#             self.map[char].add(word, index+1)
#         else:
#             self.map[char] = Trie()
#             self.map[char].add(word, index+1)
#         # print(self.map) # think trie is correct

#     # TODO: maybe i can put the wbAlgo in here? Think about elegant
            

