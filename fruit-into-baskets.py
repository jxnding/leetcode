import pdb
class Solution:
    def totalFruit(self, tree):
        def swap():
            nonlocal active
            nonlocal inactive
            active, inactive = inactive, active
        def increment():
            nonlocal basket
            nonlocal active
            basket[active]+=1
        tail = [0,0]
        ans = 0
        # Consume right-most tree
        type = [tree[-1],None]
        basket = [1,0]
        active, inactive = 0, 1
        for i in range(len(tree)-2,-1,-1):
            if tree[i]==type[active]: #fill main
                increment()
            elif type[inactive]==None: #fill secondary
                type[inactive]=tree[i]

                swap()
                increment()
            elif tree[i]==type[inactive]: #swap
                tail[inactive] = basket[inactive]
                basket[inactive] = 0

                swap()
                increment()
            else: #new secondary
                ans = max(ans, sum(basket)+sum(tail)) #store
                tail = [0, 0]
                basket[inactive]=0 #nuke
                swap()
                increment()
                type[active]=tree[i]
        ans = max(ans, sum(basket)+sum(tail))
        pdb.set_trace()
        return ans
Solution().totalFruit([1,2,3,2,2])
Solution().totalFruit([3,6,6,6,3,6,3])
#### Doesn't work
#### TODO