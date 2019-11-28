//My working solution
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
        let m = {};
        for (var i=0;i<nums.length;i++){
            if (typeof(m[nums[i]])!=='undefined'){
                // console.log("has"+i)
                if (m[nums[i]]===i) continue;
                return [m[nums[i]], i];
            } else {
                // console.log(m.keys)
                m[target-nums[i]]=i
            }
        }
        // return [9,9];
};

// Below does not work! IDK why
// EDIT: still not sure, but i do know 0===false
var twoSum = function(nums, target) {
        let m = new Map();
        let sub;
        for (var i=0;i<nums.length;i++){
            sub = target - nums[i];
            if (m.get(target-nums[i])){
                console.log("has"+i)
                // if (m.get(sub)===i) continue;
                return [m.get(sub), i];
            } else {
                // console.log(m.keys)
                m.set(sub,i)
            }
        }
        return [m.get(sub),i];
};
