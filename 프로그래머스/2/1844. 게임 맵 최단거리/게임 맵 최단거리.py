from collections import deque

def solution(maps):
  n = len(maps)
  m = len(maps[0])

  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]

  # 초기세팅 (출발지, 예정지, 방문지)
  queue = deque([(0, 0, 1)])
  answer = -1

  # 예정지가 빌 때까지
  while queue:
    # 방문
    r, c, cnt = queue.popleft()

    # 맨 끝에 도착했는지 확인
    if r == n-1 and c == m-1:
      answer = cnt
      break
  
    # 델타 탐색
    # 다음에 갈 수 있는 곳 확인하고
    for d in range(4):
      nr, nc = r+dr[d], c+dc[d]

    # 유효하다면
      if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
    # 방문체크하고
        maps[nr][nc] = 0
    # 예정지에 담기
        queue.append((nr, nc, cnt+1))

  return answer