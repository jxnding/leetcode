

double myPow(double x, int n){
    double ans = 1;
    for (int i=0;i<abs(n);i++){
        ans *= x;
    }
    if (n<0){
        return 1/ans;
    }
    return ans;
}
//O(n), slow