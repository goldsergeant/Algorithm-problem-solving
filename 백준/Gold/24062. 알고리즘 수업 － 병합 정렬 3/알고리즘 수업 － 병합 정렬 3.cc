#include <iostream>
#include <stdio.h>

using namespace std;

long long int a[1500000] = {0};
long long int tmp[1500000] = {0};
long long int cnt = 0;
long long int ans = 0;
long long int n=0,k=0;
long long int last=0;

long long int b[1500000] = {0};

int chk_same()
{
    for(;last<n;last++)
    {
        if(a[last] != b[last]) return 0;
    }
    return 1;
}



int merge(int p, int q, int r)
{
    long long int i, j, k, t;
    i = p;
    j = q+1;
    t = 1;

    while(i<=q && j<=r)
    {
        if(a[i]<=a[j])
            tmp[t++] = a[i++];
        else
            tmp[t++] = a[j++];
    }

    while(i<=q) tmp[t++] = a[i++];
    while(j<=r) tmp[t++] = a[j++];
    i=p;t=1;
    while(i <= r)
    {
       
        if(i < last) if(a[i] != tmp[t]) last = i;
        a[i++] = tmp[t++];
        if(i >= last) if(chk_same()) return 1;
    }
    return 0;
}

int merge_sort(int left, int right)
{
    int mid;
    if(left<right)
    {
        mid = (left+right)/2;
        if(merge_sort(left, mid)) return 1;
        if(merge_sort(mid+1, right)) return 1;
        if(merge(left, mid, right)) return 1;
    }
    return 0;
}

int main()
{
    int i;
    cin >> n;

    bool flag = true;
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for(int i = 0; i < n; i++)
    {
        scanf("%d",&b[i]);
    }
    for(int i = 0; i < n; i++)
    {
        if(a[i] != b[i]) flag = false;
    }
    if(flag == true)
    {
        cout << "1";
        return 0;
    }
    cout << merge_sort(0, n-1);
}