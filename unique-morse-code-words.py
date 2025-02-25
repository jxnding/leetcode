class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # N words of avg M length
        # O(N*M) runtime
        # O(N*M) space
        # longest possible collision? no such thing because we need whole string collision, no a unique prefix is enough
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        collisions = set()
        for w in words:
            # curr_str = '' #string building speed
            # for c in w:
            #     curr_str += morse[c-ord(c)]
            # collisions.add(curr_str)
            collisions.add(''.join([morse[ord(c)-ord('a')] for c in w]))
                
        return len(collisions)