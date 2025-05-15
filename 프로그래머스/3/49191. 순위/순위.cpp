#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <memory.h>
using namespace std;

int win_cnt[101];
int lose_cnt[101];
map<int,vector<int>> win_graph;
map<int,vector<int>> lose_graph;
void bfs(int start){
    queue<int> win_q;
    queue<int> lose_q;
    bool visited[101];
    memset(visited,false,sizeof(visited));
    
    win_q.push(start);
    lose_q.push(start);
    visited[start]=true;
    
    while(!win_q.empty()){
        int node =win_q.front();
        win_q.pop();
        
        for (auto adj:win_graph[node]){
            if (!visited[adj]){
                visited[adj]=true;
                win_q.push(adj);
                win_cnt[start]++;
            }
        }
    }
    
    while(!lose_q.empty()){
        int node=lose_q.front();
        if (start==2){
            cout << node<<' ';
        }
        lose_q.pop();
        
        for (auto adj:lose_graph[node]){
            if (!visited[adj]){
                visited[adj]=true;
                lose_q.push(adj);
                lose_cnt[start]++;
            }
        }
    }
    
}

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    
    for (int i=0; i<results.size();i++){
        int a =results[i][0];
        int b=results[i][1];
        
        win_graph[a].push_back(b);
        lose_graph[b].push_back(a);
    }
    
    for (int node=1; node<=n; node++){
        bfs(node);
        if (win_cnt[node]+lose_cnt[node]==n-1){
            answer++;
        }
    }
    
    return answer;
}