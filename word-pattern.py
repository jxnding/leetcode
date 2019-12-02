class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split(' ')
        if len(string)!=len(pattern): return False
        
        d = {}
        for i, c in enumerate(pattern):
            if c in d: #check if match
                if string[i]!=d[c]: return False
            else:
                # Can't bound same word to multiple variables
                if string[i] in d.values(): return False
                d[c]=string[i]
        return True #means pattern has no repeats, ex "abcd"
####