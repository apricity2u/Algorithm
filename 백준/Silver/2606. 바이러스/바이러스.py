from collections import deque

V = int(input())
E = int(input())

adj_lst = [[]*(V+1) for _ in range(V+1)]

for _ in range(E):
   s, e = map(int, input().split())
   adj_lst[s].append(e)
   adj_lst[e].append(s)

#########################################
# BFS
# 초기 세팅(출발지, 기록지, 예정지)

# 출발지는 무조건 1
queue = deque([1])
# 기록지는 방문여부를 파악하기 위해 사용
visited = [0]*(V+1)
visited[1] = 1

# 예정지가 빌 때까지
while queue:
  # 예정지에서 꺼내서 방문 (꺼내서 변수에 담는 것이 방문)
   cur = queue.popleft()

  # 방문한 곳에서 갈 수 있는 곳 탐색(인접리스트)
   for nxt in adj_lst[cur]:

   # 방문한 적이 없는 곳이라면? (기록지를 통해 알 수 있음)
      if not visited[nxt]:

      # 방문 체크하고 (탐색했을 때 방문 체크하기! 탐색 -> 방문까지 시차가 있기 때문)
         visited[nxt] = 1

      # 예정지에 집어넣는다
         queue.append(nxt)

# ans = len(visited) - 1 (집합 사용)
ans = sum(visited) - 1
   
print(ans)