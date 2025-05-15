#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(int n, int s) {
    if (n>s) return {-1};
    
    vector<int> answer;
    
    while (n){
        int tmp=ceil(s/n);
        answer.push_back(tmp);
        s-=tmp;
        n-=1;
        cout << tmp<<' ';
    }
    sort(answer.begin(),answer.end());
    return answer;
}