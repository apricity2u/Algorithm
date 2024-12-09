# 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input())

adj_lst = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

######################################

parent = [0] * (V + 1)
visited = [0] * (V + 1)


def DFS(p, cur):
    # 방문
    # parent 리스트 갱신
    parent[cur] = p

    # 탐색
    # 갈 수 있는 곳을 뽑아서 (인접리스트)
    for nxt in adj_lst[cur]:
        # 방문한적 없다면?(부모)
        if not visited[nxt]:
            # 방문체크하고
            visited[nxt] = 1
            # 방문
            DFS(cur, nxt)

DFS(0, 1)

for i in range(2, V + 1):
    print(parent[i])
