#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,m;
    cin>>n>>m;
    int arr[n];
    int sum1=0;
    int sum2=0;
    for(int i=0;i<n;i++){
        cin>>arr[i];
        if(arr[i]%m == 0) {
            sum1+=arr[i];
        }else{
            sum2+=arr[i];
        }
    }cout<<sum1-sum2;
    return 0;
}
