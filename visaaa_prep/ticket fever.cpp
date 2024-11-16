#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin>>t;
    int n,m;
    for(int i=0;i<t;i++){
        cin>>n>>m;
        if(n>=m){
            cout<<n-m<<endl;
        }
        else{
            cout<<0<<endl;
        }
    }
    return 0;
}
