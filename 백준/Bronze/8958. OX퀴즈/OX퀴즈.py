import sys
input = sys.stdin.readline

N = int(input()) 

for _ in range(N):
  result = input()

  final_score = 0
  ans = 0

  for idx in range(len(result)):
    if result[idx] == 'O':
      ans += 1
      final_score += ans
    else:
      ans = 0

  print(final_score)
