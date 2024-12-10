# 1647 도시 분할 계획

# 최소 신장트리 만들고
# 가중치가 가장 큰 간선을 빼면 자동으로 2개로 나눠짐

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 간선 가중치가 작은 순으로 정렬
edges.sort(key=lambda x : x[2])
# 0 만들고 안 쓰기
parent = [i for i in range(N+1)]

ans = 0
cnt = 0

# 간선을 하나씩 꺼내서
for a, b, w in edges:

    # 연결할 수 없다면(사이클이 생긴다면)?
    if find(a) == find(b):
        # 그냥 넘어간다    
        continue

    # 연결할 수 있다면(사이클이 생기지 않는다면)?
    # 연결하고
    union(a, b)
        # 간선 하나 세어주기
    cnt += 1
        # 가중치를 더해준다
    ans += w

    # 간선을 몇 개 뽑았는지 검토
        # N-1개 뽑았다면? => 종료
        # 두 마을로 분할해야 하기 때문에, 가중치가 가장 큰 간선을 ans에서 빼주기! 
    if cnt == N-1:
        ans -= w
        break

print(ans)