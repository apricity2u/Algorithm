import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def perm(now, depth, cost):

  global ans

  if depth == N:
    if adj_matrix[now][0]:
      cost += adj_matrix[now][0]
      ans = min(ans, cost)
      return

  for nxt in range(N):
    if not visited[nxt] and adj_matrix[now][nxt]:
      visited[nxt] = 1
      perm(nxt, depth+1, cost+adj_matrix[now][nxt])
      visited[nxt] = 0

N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0]*N
ans = float("INF")

visited[0] = 1
perm(0, 1, 0)

print(ans)