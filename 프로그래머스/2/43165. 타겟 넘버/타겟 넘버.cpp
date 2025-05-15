#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
int answer = 0;
void dfs(vector<int> &numbers,int target,int depth,int num){
    if (depth==numbers.size()){
        if (num==target) answer++;
        return;
    }
    
    dfs(numbers,target,depth+1,num-numbers.at(depth));
    dfs(numbers,target,depth+1,num+numbers.at(depth));
}

int solution(vector<int> numbers, int target) {
    dfs(numbers,target,0,0);
    return answer;
}