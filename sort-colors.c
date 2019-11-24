#include <stdio.h>
//Wrote swap myself! Mostly...
void swap(int xp, int yp) 
{ 
    int temp = xp; 
    xp = yp; 
    yp = temp; 
}
void sortColors(int A[], int n) {
    int j = 0, k = n-1;
    for (int i=0; i <= k; i++) {
        if (A[i] == 0)
            swap(A[i], A[j++]);
        else if (A[i] == 2)
            swap(A[i--], A[k--]);
    }
}
int main(){
    int input[]={2,0,2,1,1,0};
    sortColors(input,sizeof(input)/sizeof(input[0]));
    for (int i=0;i<sizeof(input)/sizeof(input[0]);i++){
        printf("%d\n",input[i]);
    }
}