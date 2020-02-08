class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(line):
            short = maxWidth-len(line)
            words = line.split(' ')
            if len(words)==1: return line+' '*(maxWidth-len(line))
            short += len(words)-1 #number of spaces removed
            i=0
            while i<short:
                for j in range(len(words)-1):
                    if i==short: break
                    words[j] += ' '
                    i+=1
            return ''.join(words)
        
        lines, curr = [], words[0]
        for i in range(1,len(words)):
            word = words[i]
            if len(curr)+1+len(word)<=maxWidth:
                curr = curr+' '+word
            else:
                lines.append(justify(curr))
                curr = word
        if curr!='': lines.append(curr+' '*(maxWidth-len(curr)))
        return lines
#### O(n), O(n); 74, 100 Python3; 80, 16 Python2
#### Tedious