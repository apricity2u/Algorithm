import sys

input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards_combis = combinations(cards, 3)
tmp = 0

for cards_combi in cards_combis:

    cards_sum = sum(cards_combi)

    if cards_sum > M:
        continue
    elif cards_sum == M:
        tmp = cards_sum
        break
    else:
        tmp = max(tmp, cards_sum)

print(tmp)
