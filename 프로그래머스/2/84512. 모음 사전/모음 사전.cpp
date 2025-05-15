#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> words;

void dfs(string cur_word){
    words.push_back(cur_word);
    if (cur_word.length()<5){
        vector<string> tmp_words ={"A","E","I","O","U"};
        for (auto ch:tmp_words)
            dfs(cur_word+ch);
    }
}

int solution(string word) {
    int answer = 0;
    vector tmp_words ={"A","E","I","O","U"};
    for (auto ch:tmp_words)
        dfs(ch);
    
    answer=distance(words.begin(),find(words.begin(),words.end(),word))+1;
    return answer;
}