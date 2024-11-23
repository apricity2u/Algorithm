# 1012 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def DFS(r,c) :
  # 방문

  # 탐색-델타탐색
  # 네 방향을 보면서
  for d in range(4):

    nr, nc = r+dr[d], c+dc[d]
    # 범위 유효성 + 1이라면
    if 0<= nr <  N and 0 <= nc < M and field[nr][nc] == 1 and (nr, nc) not in visited:
      # 방문 체크하고
      visited.add((nr, nc))
      # 방문
      DFS(nr, nc)
  

for _ in range(T):
  M, N, K = map(int, input().split())
  field = [[0]*M for _ in range(N)]

  for _ in range(K):
    c, r = map(int, input().split())
    field[r][c] = 1

  visited = set()
  ans = 0

  # 순회하며
  for r in range(N):
    for c in range(M):

    # 1이고, 방문한적 없다면?
      if field[r][c] == 1 and (r, c) not in visited:
      # DFS 또는 BFS
      # 방문지에 넣어줘야함
        visited.add((r,c))
        DFS(r, c)
      # 정답 +1
        ans += 1

  print(ans)