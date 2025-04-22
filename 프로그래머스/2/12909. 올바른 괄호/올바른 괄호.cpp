#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> stack;
    
    for (int i=0;i<s.length();i++){
        if (stack.empty()){
            stack.push('(');
            continue;
        }
        
        if (s[i]=='('){
            stack.push('(');
        }else{
            if (!stack.empty() && stack.top()=='('){
                stack.pop();
            }else{
                return false;
            }
        }
    }

    return stack.empty();
}