import sys
input = sys.stdin.readline

N = int(input())

words = set(input().strip() for _ in range(N))

sorted_words = sorted(words, key=lambda x: (len(x), x))

for sorted_word in sorted_words:
  print(sorted_word)
