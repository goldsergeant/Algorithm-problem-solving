#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <climits>
using namespace std;

map<int,vector<pair<int,int>>> graph;
int dist[51];

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    fill(dist,dist+51,INT_MAX);
    
    for (auto arr:road){
        int a = arr[0];
        int b=arr[1];
        int cost=arr[2];
        
        graph[a].push_back(make_pair(b,cost));
        graph[b].push_back(make_pair(a,cost));
    }
    
    priority_queue<pair<int,int>,vector<pair<int,int>>, greater<pair<int,int>>> heap;
    heap.push(make_pair(0,1));
    dist[1]=0;
    
    while (!heap.empty()){
        int curCost=heap.top().first;
        int curNode=heap.top().second;
        heap.pop();
        
        for (auto p:graph[curNode]){
            int adjNode=p.first;
            int adjCost=p.second;
            if (dist[adjNode]>curCost+adjCost){
                dist[adjNode]=curCost+adjCost;
                heap.push(make_pair(dist[adjNode],adjNode));
            }
        }
    }
    
    for (int node=1; node<=N; node++){
        cout << dist[node] << ' ';
    }
    for (int node=1;node<=N;node++){
        if (dist[node]<=K)
            answer++;
    }

    
    return answer;
}