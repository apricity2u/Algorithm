import sys

input = sys.stdin.readline

N, M = map(int, input().split())

groups = dict()

for _ in range(N):

    group = input().rstrip()
    members_total = int(input())
    members = list(input().rstrip() for _ in range(members_total))
    members.sort()

    groups[group] = members

for _ in range(M):
    question = input().rstrip()
    question_type = int(input())

    if question_type == 0:
        print(*groups[question], sep="\n")
    elif question_type == 1:

        for group, members in groups.items():

            if question in members:
                print(group)