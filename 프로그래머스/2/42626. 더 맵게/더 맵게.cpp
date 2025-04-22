#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq;

    for (auto n : scoville)
    {
        pq.push(n);
    }

    while (!pq.empty())
    {
        int a = pq.top();
        if (a>=K){
            return answer;
        }
        pq.pop();

        if (pq.empty())
        {
            return -1;
        }
        int b = pq.top();
        pq.pop();
        pq.push(a + (b * 2));
        answer++;
    }
    return answer;
}
