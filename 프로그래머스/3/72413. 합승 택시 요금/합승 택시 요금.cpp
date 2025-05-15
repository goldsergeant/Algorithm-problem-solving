#include <string>
#include <vector>
#include <climits>
#include <algorithm>
#include <map>
#include <queue>
#include <iostream>

using namespace std;
map<int,vector<pair<int,int>>> graph;
int dist[201];

int dijkstra(int start,int end){
    fill(dist,dist+201,INT_MAX);
    
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> heap;
    heap.push(make_pair(0,start));
    dist[start]=0;
    
    while(!heap.empty()){
        pair<int,int> p=heap.top();
        heap.pop();
        int curCost=p.first;
        int curNode=p.second;
        
        if (curNode==end){
            return curCost;
        }
        
        if (curCost>dist[curNode]){
            continue;
        }
        
        for (auto adjP:graph[curNode]){
            int adjNode=adjP.first;
            int adjCost=adjP.second;
            
            if (dist[adjNode]>adjCost+curCost){
                dist[adjNode]=adjCost+curCost;
                heap.push(make_pair(dist[adjNode],adjNode));
            }
        }
    }
    return INT_MAX;
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = INT_MAX;
    
    for(auto arr:fares){
        int a =arr[0];
        int b=arr[1];
        int cost=arr[2];
        
        graph[a].push_back(make_pair(b,cost));
        graph[b].push_back(make_pair(a,cost));
        
    }
    
    for (int middleNode=1; middleNode<=n;middleNode++){
        answer=min(answer,dijkstra(s,middleNode)+dijkstra(middleNode,a)+dijkstra(middleNode,b));
    }
    return answer;
}