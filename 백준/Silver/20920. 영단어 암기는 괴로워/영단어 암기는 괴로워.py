import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = dict()

for _ in range(N):
    
    word = input().rstrip()

    if len(word) < M:
        continue

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sorted_words = sorted(words, key=lambda x: (-words[x], -len(x), x))

print(*sorted_words, sep="\n")