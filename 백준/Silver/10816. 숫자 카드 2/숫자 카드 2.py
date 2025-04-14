import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
num_cards = list(map(int, input().split()))

card_counter = Counter(num_cards)

M = int(input())
nums = list(map(int, input().split()))

answer = []

for num in nums:
    
    if num in card_counter:
        answer.append(card_counter[num])
    else:
        answer.append(0)

print(*answer)