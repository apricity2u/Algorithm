import sys
input = sys.stdin.readline

N, M = map(int,input().split())
names = {}

for _ in range(N + M):
    name = input().rstrip()

    if name in names:
        names[name] += 1
    else:
        names[name] = 1

answer = []

for name, counts in names.items():
    if counts == 2:
        answer.append(name)

# answer = [name for name, counts in names.items() if counts == 2]

answer.sort()

print(len(answer))
print(*answer, sep="\n")
# print("\n".join(answer))