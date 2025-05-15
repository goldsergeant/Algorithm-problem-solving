#include <string>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    for (int i=0; i<prices.size(); i++) answer.push_back(0);
    stack<pair<int,int>> stack;
    
    for (int i=0; i<prices.size();i++){
        while (!stack.empty()&& stack.top().second>prices[i]){
            int index=stack.top().first;
            stack.pop();
            answer[index]=i-index;
        }
        stack.push(make_pair(i,prices[i]));
    }
    while (!stack.empty()){
        int index=stack.top().first;
        stack.pop();
        answer[index]=prices.size()-index-1;
    }
    return answer;
}