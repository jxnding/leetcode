class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## Build graph
        ## Toposort
        # Find the source nodes, expand...

        def toposort(front, depth):
            if len(front) == 0: return False
            if depth > len(allchars)-1: return True # cycle exists
            
            nextFront = set()
            for char in front:
                # update the topoindex
                nonlocal topoindex
                topoindex[char] = depth #update to the latest (biggest) depth
                # next front
                for neighbor in graph[char]:
                    nextFront.add(neighbor)

            return toposort(nextFront, depth+1)
                

        ## Build graph (directed), 26 letters
        # Dict.keys for stableset
        # graph = [set() for _ in range(26)]
        
        # all chars
        allchars = set()
        for word in words:
            for w in word:
                allchars.add(w)
        # build graph 
        sources = allchars.copy()
        graph = collections.defaultdict(set)
        for word in words:
            for i in range(1, len(word)):
                char1, char2 = word[i-1], word[i]
                graph[char1].add(char2)
                # Find sources (islands will be included)
                if char2 in sources:
                    sources.remove(char2)
        
        # # Find sources
        # sources = set(graph.keys())
        # for key, value in graph.items():
        #     if value in sources:
        #         sources.remove(value)

        if len(sources) == 0: return ''

        ## Toposort
        topoindex = {key: None for key in allchars}
        cycleExists = toposort(sources, 0)
        if cycleExists: return ''

        ## Sort and return
        topolist = [[char, index] for char, index in topoindex.items()]
        topolist.sort(key=lambda x:x[1])
        return ''.join([x[0] for x in topolist])
### Ah fuck I misunderstood the problem. I thought every word is in lexi order. Not the order of the words...