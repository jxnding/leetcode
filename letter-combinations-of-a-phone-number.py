class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def getLetters(n):
            if n==9: return ['w','x','y','z']
            if n==8: return ['t','u','v']
            if n==7: return ['p','q','r','s']
            n = (n-2)*3 + 97
            return [chr(n),chr(n+1),chr(n+2)]
        def combo(s):
            if len(s)==1: return getLetters(int(s))
            prev = combo(s[1:])
            curr = []
            for c in getLetters(int(s[0])):
                for p in prev:
                    curr.append(c+p)
            return curr
        if len(digits)<1: return []
        return combo(digits)
#### O(exp), O(exp); 88, 100 Python3
#### Could be cleaner