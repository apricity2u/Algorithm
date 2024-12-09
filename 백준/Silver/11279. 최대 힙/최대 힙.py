from heapq import heappop, heappush, heapify

import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

heap = []

for num in nums:
    if num > 0 :
        heappush(heap, -num)
    elif num == 0 :

        if len(heap) == 0 :
            print(0)
            continue

        print(-heappop(heap))
