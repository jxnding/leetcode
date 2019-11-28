class Solution {
    public int[] twoSum(int[] numbers, int target) {
        boolean found = false;

        int small = 0;
        int big = numbers.length-1;
        while(!found){
            int sum = numbers[small]+numbers[big];
            if(sum==target){
                return new int[] {small+1,big+1};
            }
            // too big
            else if(sum>target){
                int newsum = numbers[small]+numbers[big-1];
                if(newsum==target)
                    return new int[] {small+1,big-1+1};
                else if(newsum>target)
                    big--;
                else
                    small++;

            // too small
            } else {
                int newsum = numbers[small+1]+numbers[big];
                if(newsum==target)
                    return new int[] {small+1+1,big+1};
                else if(newsum<target)
                    small++;
                else
                    big--;
            }
        }

        return new int[] {0,0};
    }
}
