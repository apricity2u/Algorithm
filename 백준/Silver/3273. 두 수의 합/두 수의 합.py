import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

i = 0
j = N-1
tmp = 0
ans = 0

while True:

  if i == j:
    break

  tmp = nums[i] + nums[j]

  if tmp < x:
    tmp -= nums[i]
    i += 1

  elif tmp > x:
    tmp -= nums[j]
    j -= 1

  elif tmp == x:
    ans += 1
    tmp -= nums[i]
    i += 1

print(ans)