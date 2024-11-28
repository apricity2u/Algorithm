import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0]*N
ans = []

def perm(depth):

  if depth == M:
    print(*ans)
    return

  for idx in range(N):

    if not visited[idx]:
      visited[idx] = 1
      ans.append(nums[idx])

      perm(depth+1)
      
      ans.pop()
      visited[idx] = 0
      
perm(0)