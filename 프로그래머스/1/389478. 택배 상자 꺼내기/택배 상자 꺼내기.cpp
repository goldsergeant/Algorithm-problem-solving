int boxes[100][10] = {0};

int solution(int n, int w, int num)
{
    int answer=0;
    int row = 0;
    int col = 0;

    int cur = 1;
    int dir = 1;
    while (cur <= n)
    {
        boxes[row][col] = cur++;
        col += dir;
        if (col == w || col == -1)
        {
            col -= dir;
            dir *= -1;
            row++;
        }
    }

    int target_r=0;
    int target_c=0;
    for (int i=0; i<n;i++){
        for (int j=0; j<w; j++){
            if (boxes[i][j]==num){
                target_r=i;
                target_c=j; 
            }
        }
    }

    while (boxes[target_r][target_c]!=0){
        answer++;
        target_r++;
    }
    return answer;
}
