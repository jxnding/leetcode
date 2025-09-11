VOWELS = set(['a', 'e', 'i','o','u'])
class Solution:
    def sortVowels(self, s: str) -> str:
        ## Guards
        # Check all values are letters

        # lEetcOde
        # _XX__X_X
        # 01234567
        # lEOtcede
        # 01534267

        ## Sort vowels
        # Loop and pop to build a new string
        vowels = [c for c in s if c.lower() in VOWELS]
        vowels.sort(reverse=True) # we will pop, which removes & returns the last element

        ans = [c if c.lower() not in VOWELS else vowels.pop() for c in s]
        
        return ''.join(ans)