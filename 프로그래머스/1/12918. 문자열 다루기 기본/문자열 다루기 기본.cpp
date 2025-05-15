#include <string>
#include <vector>
#include <ctype.h>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if (s.length()!=4 && s.length()!=6){
        return false;
    }
    for (auto ch:s){
        if (!isdigit(ch)){
            return false;
        }
    }
    return answer;
}