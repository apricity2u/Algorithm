# 1697 숨바꼭질 (BFS)

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

# 구조화

# 초기세팅 (출발지, 예정지, 기록지)
queue = deque([(N, 0)])   # 이동 예정지 (X-1, X+1)
visited = set([N])   # X

# 예정지가 빌 때까지
while queue:
  # 방문
  cur, cnt = queue.popleft()

  # K에 도착했는지 확인
  if cur == K:
    break

  # 탐색
  # cur*2가 무한대로 커지기 때문에, nxt 값을 적당히 범위를 정해줘야함
  for nxt in [cur+1, cur-1, cur*2]:
    if 0 <= nxt <= 140000 and nxt not in visited:
      queue.append((nxt, cnt+1))
      visited.add((nxt))

print(cnt)