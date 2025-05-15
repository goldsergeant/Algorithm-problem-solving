#include<vector>
#include<map>
#include<queue>
#include<tuple>
#include<iostream>
using namespace std;
int dr[] ={1,0,-1,0};
int dc[]= {0,1,0,-1};

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    bool visited[100][100];
    fill(visited[0],visited[100],false);
    queue<tuple<int,int,int>> q;
    visited[0][0]=true;
    q.push(make_tuple(0,0,1));
    
    while (!q.empty()){
        int r=get<0>(q.front());
        int c=get<1>(q.front());
        int cnt=get<2>(q.front());
        q.pop();
        
        if (r==maps.size()-1 && c==maps.at(0).size()-1) return cnt;
        
        for (int i=0; i<4;i++){
            int nr=r+dr[i];
            int nc=c+dc[i];
            
            if (nr<0 || nc<0 || nr>=maps.size() || nc>=maps[0].size()) continue;
            if (visited[nr][nc]) continue;
            if (!maps[nr][nc]) continue;
            
            q.push(make_tuple(nr,nc,cnt+1));
            visited[nr][nc]=true;
        }
        }
    return -1;
}