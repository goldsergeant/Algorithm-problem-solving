import collections
import sys


def solution(sales, links):
    sales = [0] + sales
    graph = collections.defaultdict(list)
    for num, under in links:
        graph[num].append(under)

    dp = [[sys.maxsize, sys.maxsize] for i in range(len(sales))]

    def dfs(node):
        if not graph[node]: #리프노드
            return sales[node],0

        if dp[node] != [sys.maxsize, sys.maxsize]:
            return dp[node][0], dp[node][1]

        sum_child = 0
        for under in graph[node]:
            include, not_include = dfs(under)
            sum_child += min(include, not_include)

        dp[node][0] = sum_child + sales[node]
        # dp[node][1] = sales[node]

        for under in graph[node]:
            include, not_include = dfs(under)
            if include<not_include:
                dp[node][1]=min(dp[node][1],sum_child)
            else:
                dp[node][1]=min(dp[node][1],sum_child+include-not_include)

        return dp[node][0], dp[node][1]
    return min(dfs(1))


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
# print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
# print(solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
# print(solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]))
