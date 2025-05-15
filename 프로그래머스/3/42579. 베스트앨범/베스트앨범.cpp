#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <memory.h>
#include <iostream>

using namespace std;
int song_play_time[10000];
map<string,int> genre_play_time;

bool compare1(int a, int b){
    return song_play_time[a]>song_play_time[b];
}
bool compare2(string a,string b){
    return genre_play_time[a]>genre_play_time[b];
}
vector<int> solution(vector<string> genres, vector<int> plays) {

    memset(song_play_time,0,sizeof(song_play_time));
    vector<int> answer;
    map<string,vector<int>> genre_songs;
    set<string> genres_set(genres.begin(),genres.end());
    vector<string> genres_vector;
    for (int i=0; i<genres.size();i++){
        genre_play_time[genres[i]]+=plays[i];
        song_play_time[i]+=plays[i];
        genre_songs[genres[i]].push_back(i);
    }
    for (auto& iter:genre_songs){
        vector tmp = iter.second;
        sort(iter.second.begin(),iter.second.end(),compare1);
    }
    for (auto genre:genres_set){
        genres_vector.push_back(genre);
    }
    
    sort(genres_vector.begin(),genres_vector.end(),compare2);
    
    for (auto genre: genres_vector){
        vector tmp = genre_songs[genre];
        int cnt=0;
        for (auto song:tmp){
            if (cnt==2){
                break;
            }
            
            cnt++;
            answer.push_back(song);
        }
    }
    return answer;
}