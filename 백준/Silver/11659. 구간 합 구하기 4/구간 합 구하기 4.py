import sys
input = sys.stdin.readline

from itertools import accumulate

N, M = map(int, input().split())
nums = list(map(int, input().split()))

acc = [0] + list(accumulate(nums))

for _ in range(M):
  i, j = map(int, input().split())
  print(acc[j] - acc[i-1])