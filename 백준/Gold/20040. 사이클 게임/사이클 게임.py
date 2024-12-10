# 20040 사이클 게임

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    # 루트노드 : 자신의 인덱스 값과 원소값이 같음
    # 인덱스 != 원소가 같지 않을 때까지 : 루트 노드를 찾을 때까지 반복.

    # 재귀함수를 사용하여 루트노드를 찾고 다시 돌아오면서 부모노드들을 루트노드로 변경

    if x != parent[x]:
        parent[x] = find(parent[x])

    # 여기서 루트노드인 5라는 값이 계속 return됨
    return parent[x]


def union(x, y):

    # find를 바꾸면 하기만 써도 됨
    if find(x) != find(y):
        # x의 루트노드를 찾아서, 그 부모를 y의 루트노드로 변경해서 연결한다.
        parent[find(x)] = find(y)


n, m = map(int, input().split())
# 0부터 n-1까지 자신을 부모노드로 가짐 (다 떨어져있다)
parent = list(range(n))


for cnt in range(1, m + 1):
    a, b = map(int, input().split())

    # 이미 연결 관계가 있다면
    if find(a) == find(b):
        print(cnt)
        break

    # 아니면 유니온!
    union(a, b)

else:
    print(0)
