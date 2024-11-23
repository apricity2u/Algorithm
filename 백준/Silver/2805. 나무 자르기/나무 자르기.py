import sys
input = sys.stdin.readline

def check_length(h):
    return sum([i - h for i in trees if i > h])

N, M = map(int, input().split())

trees = list(map(int, input().split()))

l, r = 0, 1000000000
c = (l + r) // 2                # 최초의 기준

while l <= r:
    cnt = check_length(c)

    if cnt >= M:                # 현재 기준으로 자를 수 있는 나무가 너무 많으면
        l = c + 1               # l포인터를 c+1로 올리고

    else:                       # 자를 수 있는 나무가 너무 적으면
        r = c - 1               # r포인터를 c-1로 내리고

    c = (l + r) // 2            # 새로운 기준 설정

print(c)