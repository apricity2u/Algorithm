from heapq import heappop, heappush, heapify

import sys
input = sys.stdin.readline

N = int(input())
cards = list(int(input()) for _ in range(N))

heapify(cards)
tmp = 0
min_cnt = 0

while cards:

    if len(cards) == 1:
        break

    tmp = heappop(cards)
    tmp += heappop(cards)
    heappush(cards, tmp)
    min_cnt += tmp

print(min_cnt)