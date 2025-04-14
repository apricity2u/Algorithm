import sys
input = sys.stdin.readline

N = int(input())
num_cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

answer = {}

for num in num_cards:
    
    if num in answer:
        answer[num] += 1
    else:
        answer[num] = 1

answer2 = []

for num in nums:

    if num in answer:
        answer2.append(answer[num])
    else: 
        answer2.append(0)

print(*answer2)