#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> heap;
    queue<pair<int,int>> q;
    for (int i=0; i<priorities.size();i++){
     heap.push(priorities[i]);
        q.push(make_pair(i,priorities[i]));
    }    
    int execute_order=1;
    while (!q.empty()){
        int index=q.front().first;
        int value=q.front().second;
        q.pop();
        if (value==heap.top()){
            heap.pop();
            if (location==index) return execute_order;
            execute_order++;
        }else{
            q.push(make_pair(index,value));
        }
    }
    return answer;
}