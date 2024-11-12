import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

i = j = 0

tmp = ans = 0

while True:

  if tmp < M:
    if j == N:
      break
    tmp += nums[j]
    j += 1

  elif tmp > M:
    tmp -= nums[i]
    i += 1

  elif tmp == M:
    ans += 1
    tmp -= nums[i]
    i+=1

print(ans)