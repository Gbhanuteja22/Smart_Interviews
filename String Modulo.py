#include <bits/stdc++.h>
#include<iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        string n;
        long long p;
        cin>>n>>p;
        long long res=0;
        for(char ch:n){
            res=(res*10+(ch-'0'))%p;
        }
        cout<<res<<endl;
    }
    return 0;
}
