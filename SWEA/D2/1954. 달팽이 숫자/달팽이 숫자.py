T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):

  N = int(input())
  
  # N * N 짜리 빈 판 제작
  snail = [[0]*N for _ in range(N)]

  # 초기값 세팅
  r, c = 0, 0
  d = 0

  # 1 ~ N*N까지 반복하며
  for num in range(1, N**2+1):
    # r, c에 숫자 입력
    snail[r][c] = num

    # 새로운 좌표 찍기(nr, nc)
    nr, nc = r+dr[d], c+dc[d]
    # 좌표 유효성 검사(범위, 방문 여부)
    
    # 유효? => 이동
    if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
      r, c = nr, nc
      continue

      # 유효X => 방향 전환 => 새로운 좌표 이동
    d = (d+1)%4
    nr, nc = r+dr[d], c+dc[d]
    r, c = nr, nc
      
  print(f'#{tc}')
  for line in snail:
    print(*line)