# 1717 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    # 루트노드 : 자신의 인덱스 값과 원소값이 같음
    # 인덱스 != 원소가 같지 않을 때까지 : 루트 노드를 찾을 때까지 반복.

    # 시간복잡도 : 트리의 깊이 
    # 시간복잡도를 줄이기 위해 트리의 깊이를 줄여야함!
    # 재귀함수를 사용하여 루트노드를 찾고 다시 돌아오면서 부모노드들을 루트노드로 변경

    # parent = [2, 2, 3, 4, 5, 5, 4, 4]

    if x != parent[x]:
        parent[x] = find(parent[x])

    # 여기서 루트노드인 5라는 값이 계속 return됨
    return parent[x]

def union(x, y):

    # find를 바꾸면 하기만 써도 됨
    # if find(x) != find(y):
        # x의 루트노드를 찾아서, 그 부모를 y의 루트노드로 변경해서 연결한다.
    parent[find(x)] = find(y)

    # 다른 집합인 경우. (서로 다른 루트 노드를 가진 경우)
    # 더 작은 트리를 더 큰 트리에 붙이면 됨!

    # if find(x) != find(y):
    #     # x의 루트노드를 찾아서, 그 부모를 y의 루트노드로 변경해서 연결한다.
    #     # rank라는 보조 리스트를 통해, 각각의 깊이를 기록 (대신 find 연산을 변경하면 없어도 됨..)
    #     # rank를 늘려줄 필요가 없음 : 어차피 큰 트리에 작은 트리를 붙여서 변화없음
    #     if rank[find(x)] > rank[find(y)]:
    #         parent[find(y)] = find(x)
    #     elif rank[find(x)] < rank[find(y)]:
    #         parent[find(x)] = find(y)
    #     else:
    #         # 대신 깊이가 같을 때는 깊이가 한 칸만 깊어짐
    #         parent[find(x)] = find(y)
    #         rank[find(y)] += 1
        
    #     parent[find(x)] = find(y)

n, m = map(int, input().split())

# 트리 만들기 (자신의 인덱스를 원소로 가짐 : 모든 노드들이 다 떨어진 형태의 트리)
parent = list(range(n+1))

for _ in range(m):
    c, a, b = map(int, input().split())
    
    # 깊이를 기록할 보조 리스트
    # rank = [0] * (n+1)

    if c == 0:
        union(a, b)

    elif c == 1:
        # 서로의 루트 노드를 찾기
        if find(a) == find(b):
            print("yes")
        else:
            print("no")