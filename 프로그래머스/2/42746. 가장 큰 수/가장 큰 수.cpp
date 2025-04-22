#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool compare(int a, int b){
    string string_a=to_string(a);
    string string_b=to_string(b);
    return string_a+string_b>string_b+string_a;
}

string solution(vector<int> numbers) {
    string answer = "";
    sort(numbers.begin(),numbers.end(),compare);
    for (auto n:numbers){
        answer.append(to_string(n));
    }
    if (answer== string(answer.length(),'0')){
        answer='0';
    }
    return answer;
}