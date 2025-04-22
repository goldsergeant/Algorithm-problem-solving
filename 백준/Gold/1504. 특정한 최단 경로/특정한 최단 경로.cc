#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <map>

using namespace std;
vector<pair<int, int>> graph[801];
typedef tuple<int, int, int> T;
int dist[801][1 << 2];
const int INF= 2e9;
const int END_BIT = 1 << 1 | 1;
int main()
{
    int N, E;
    int v1, v2;
    cin >> N >> E;
    fill(&dist[0][0], &dist[N][1 << 2], INF);

    for (int i = 0; i < E; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back(make_pair(b, c));
        graph[b].push_back(make_pair(a, c));
    }
    cin >> v1 >> v2;

    priority_queue<T, vector<T>, greater<T>> q;
    if (v1==1 || v2==1){
        q.push(make_tuple(0, 1, v1==1?1:1<<1));
    }else{
        q.push(make_tuple(0, 1, 0));
    }
    dist[1][0] = 0;
    while (!q.empty())
    {
        auto [cost, node, bit] = q.top();
        q.pop();
        if (node == N && bit == END_BIT)
        {
            cout << cost;
            return 0;
        }

        if (dist[node][bit] < cost)
            continue;

        for (auto [n_node, n_cost] : graph[node])
        {
            if (n_node == v1 || n_node == v2)
            {
                int bit2 = n_node == v1 ? 1 : 1 << 1;
                int n_bit = bit | bit2;
                if (cost + n_cost < dist[n_node][n_bit])
                {
                    dist[n_node][n_bit] = cost + n_cost;
                    q.push(make_tuple(cost + n_cost, n_node, n_bit));
                }
            }
            else
            {
                if (cost + n_cost < dist[n_node][bit])
                {
                    dist[n_node][bit] = cost + n_cost;
                    q.push(make_tuple(cost + n_cost, n_node, bit));
                }
            }
        }
    }
    cout << -1;

    return 0;
}