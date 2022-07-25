#include <set>

class Solution {
public:
    char repeatedCharacter(string s) {
        // std::set mySet = new std::set<string>(); doesn't work, why?
        std::set<char> mySet;
         for (char const c: s){
            if (mySet.count(c))
                return c;
            else
                mySet.insert(c);
         }
        return 'a';//make sure to return
    }
};