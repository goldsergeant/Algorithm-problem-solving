#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion)
{
    string answer = "";
    map<string, int> counter;
    for (int i = 0; i < participant.size(); i++)
    {
        counter[participant[i]]++;
    }

    for (int i=0; i<completion.size(); i++){
        counter[completion[i]]--;
    }

    for (auto iter=counter.begin();iter!=counter.end();iter++)
    {
        if (iter->second>0){
            answer=iter->first;
            break;
        }
    }
    return answer;
}