int largestRectangleArea(int* heights, int heightsSize){
    int maxArea = 0;
    for(int i=0; i<heightsSize; i++){
        int l = i;
        for (int j=i;j>=0;j--){
            if (heights[j]<heights[i]){
                l = j+1;
                break;
            }
            l = j;
        }
        int r = i;
        for (int j=i;j<heightsSize;j++){
            if (heights[j]<heights[i]){
                r = j-1;
                break;
            }
            r = j;
        }
        if ((r - l + 1)*heights[i] > maxArea){
            maxArea = (r - l + 1)*heights[i];
        }
    }
    return maxArea;
}
// O(n^2), O(1); 6, 100
// TODO: Not optimal!

