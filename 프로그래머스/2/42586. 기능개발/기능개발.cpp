#include <string>
#include <vector>
#include <deque>
#include <iostream>


using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int day=0;
    int clearCount=0;
    for (int i =0; i<progresses.size();i++){
        int progress=progresses.at(i);
        int speed=speeds.at(i);
        bool alreadyClear=true;
        progress+=speed*day;
        
        if (progress>=100){
            clearCount++;
            continue;                        
        }else{
            if (i!=0) answer.push_back(clearCount);
            clearCount=1;
            
        }
        
        while (progress<100){
            day+=1;
            progress+=speed;
        }
        
    }
    answer.push_back(clearCount);
    return answer;
}