import sys
input = sys.stdin.readline

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

M, N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

queue = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1: queue.append((r, c))               

while queue:                                                    
    r, c = queue.popleft()                                     
    for d in range(4):                                         
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:  
            board[nr][nc] = board[r][c] + 1                    
            queue.append((nr, nc))                              

ans = -1

for row in board:                                               
    if row.count(0) > 0:                                        
        ans = 0                                                 
        break
    ans = max(row + [ans])                                      

print(ans - 1)   