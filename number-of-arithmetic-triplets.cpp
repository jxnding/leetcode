class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        // helper function that while loops forward to find next pair
        // if return == input, then there is none
        auto look_forward = [&nums, &diff](int input) -> int {
            int i = input+1;
            while(i < nums.size())
                if (nums[i] - nums[input] == diff)
                    return i;
                else
                    i++;
            return input;
        };
        
        int ans = 0;
        // look for beginning of triplets, so end at size-2
        for (int i=0; i<nums.size()-2; i++){
            int output = look_forward(i);
            if (output != i && look_forward(output) != output)
                ans++;
        }
        return ans;
    }
};
/** 
TODO: think if this is optimal... Brain too foggy rn.
Potentially can optimize seconds (aka j's) away with a list and deleting that item from list. But this is like only 1/3 of the numbers
Maybe go backwards? probably not
*/