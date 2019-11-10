class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def good(word):
            currSet = charSet
            for c in word:
                if c in currSet:
                    currSet[c]-=1
                    if currSet[c]==-1:
                        return False
                else:
                    return False
            return True
        
        charSet = {}
        for c in chars:
            if c in charSet:
                charSet[c]+=1
            else:
                charSet[c]=1
        
        goodSum = 0
        for word in words:
            if good(word):
                goodSum+=len(word)
        return goodSum
            
                        