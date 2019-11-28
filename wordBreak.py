def wordBreak(self, s, wordDict):
    ans = False
    def wh(s):
        if len(s)==0:
            nonlocal ans
            ans = True
            return
        nonlocal wordDict
        for word in wordDict:
            if s[0:len(word)] == word:
                wh(s[len(word):])
    if len(s)==0 or len(wordDict)==0:
        return False
    wh(s)
    return ans

class Solution:
    def wordBreak(self, s, wordDict):
        ###
        inputset = set(s)
        wordset = set()
        for word in wordDict:
            wordset.union(set(word))
        if len(inputset.difference(wordset))>0:
            return False
        ###
        ans = False
        wordDict.sort(reverse=True)
        def wh(s):
            nonlocal ans
            if ans:
                return ans
            if len(s)==0:
                ans = True
                return
            nonlocal wordDict
            for word in wordDict:
                if s[0:len(word)] == word:
                    wh(s[len(word):])
        if len(s)==0 or len(wordDict)==0:
            return False
        wh(s)
        return ans
