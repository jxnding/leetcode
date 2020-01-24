class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace('\'',' ')
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.lower()
        banned = set(banned)
        
        words = {}
        for word in paragraph.split(' '):
            if word=='' or word in banned: continue
            if word in words:
                words[word]+=1
            else:
                words[word]=1
        
        maxCount, maxWord = -1, ""
        for word, count in words.items():
            if count>maxCount:
                print("Waka"+word)
                maxCount = count
                maxWord = word
        print(words)
        print(banned)
        return maxWord

#### O(n+m), O(n), n=paragraph, m=banned; 88, 100 Python3
#### Stupid question
#### TODO: Regex and collections are programmatically useful. See below
# https://leetcode.com/problems/most-common-word/discuss/123854/C%2B%2BJavaPython-Easy-Solution-with-Explanation
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]