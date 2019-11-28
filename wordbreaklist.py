def wordBreak2(self, s, wordDict):
    ans = []
    def wh(t,s):
        if len(s)==0:
            nonlocal ans
            ans.append(t.strip())
        else:
            nonlocal wordDict
            for word in wordDict:
                if s[:len(word)] == word:
                    wh(t+" "+s[:len(word)],s[len(word):])
    if len(s)==0 or len(wordDict)==0:
        return []
    wh("",s)
    ans.sort()
    return ans[::-1]
