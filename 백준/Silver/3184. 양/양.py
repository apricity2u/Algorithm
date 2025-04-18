# 3184 양 
# (방문지 = 원본 배경 변경하기)
# (패딩을 만들어주기 (빈 배열))

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# DFS
def DFS(r, c):
  # 출발지, 예정지, 임시양, 임시늑대
  stack = [(r, c)]
  tmp_o, tmp_v = 0, 0
 
  if field[r][c] == 'o':
    tmp_o += 1
  elif field[r][c] == 'v':
    tmp_v += 1

  # 임시양과 늑대 수를 더해준 다음에 울타리로 변경하기
  field[r][c] = "#"

  # 예정지가 빌 때까지
  while stack:
  # 방문
    r, c = stack.pop()

  # 탐색 - 델타 탐색
    # 4방향을 탐색하며
    for d in range(4):
      # 새로운 좌표를 찍어보고
      nr, nc = r+dr[d], c+dc[d]
      # 갈 수 있다면(범위, 울타리X, 방문X )
      if field[nr][nc] != "#":
        # 양인지, 늑대인지
          if field[nr][nc] == 'o':
            tmp_o += 1
          elif field [nr][nc] == 'v':
            tmp_v += 1
        # 방문체크하고
          field[nr][nc] = '#'
        # 예정지에 담기(스택)
          stack.append((nr, nc))

  # 임시양ㅇ, 임시늑대 비교해서 리턴
  if tmp_o > tmp_v:
    return tmp_o, 0
  else:
    return 0, tmp_v


R, C = map(int, input().split())
field = [['#']*(C+2) for _ in range(R+2)]
for i in range(1,R+1):
  field[i][1:C+1] = list(input().rstrip())

# 초기 세팅 (출발지, 기록지, 예정지)
  # 출발지는 방문한 곳이 자동으로 출발지가 됨
  # 예정지는 DFS를 돌 때마다 갱신
  # 기록지는 전체가 공유하는 것

o_cnt, v_cnt = 0, 0

# field를 순회하며
for r in range(1,R+1):
  for c in range(1,C+1):
  # 울타리도 아니고, 방문한적도 없다면
    if field[r][c] != '#':
      # 방문 + DFS
      tmp_o, tmp_v = DFS(r, c)
      # 결과를 전체 양, 늑대 개수에 반영
      o_cnt += tmp_o
      v_cnt += tmp_v

print(o_cnt, v_cnt)