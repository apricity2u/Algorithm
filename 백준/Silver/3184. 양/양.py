import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global lambs, wolves
    lambs_tmp, wolves_tmp = 0, 0
    queue = deque([(r, c)])     # 첫 좌표 큐에 넣기

    if field[r][c] == 'o':      # 양 세기
        lambs_tmp += 1
    elif field[r][c] == 'v':    # 늑대 세기
        wolves_tmp += 1

    field[r][c] = '#'           # 검토한 곳은 울타리로 닫기

    while queue:                # 큐가 빌 때까지 BFS
        r, c = queue.popleft()

        for d in range(4):                  # 4방 탐색하며
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < R and 0 <= nc < C and field[nr][nc] != '#':
                if field[nr][nc] == 'o':    # 양 세고
                    lambs_tmp += 1
                elif field[nr][nc] == 'v':  # 늑대 세고
                    wolves_tmp += 1

                field[nr][nc] = '#'         # 좌표 닫기
                queue.append((nr, nc))
    
    if lambs_tmp > wolves_tmp:              # 양이 더 많으면
        lambs += lambs_tmp                  # 양 추가
    else:                                   # 아니라면
        wolves += wolves_tmp                # 늑대 추가


R, C = map(int, input().split())

field = [list(input().rstrip()) for _ in range(R)]

lambs = 0
wolves = 0

for r in range(R):
    for c in range(C):
        if field[r][c] != '#':
            bfs(r, c)


print(lambs, wolves)