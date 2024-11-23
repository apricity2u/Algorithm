# 9012 괄호
from collections import deque

import sys
input = sys.stdin.readline

for _ in range(int(input())):

  words = input().rstrip()
  queue = deque()

  for word in words:
    if word == '(':
      queue.append(word)
    
    elif queue:
      queue.popleft()

    else:
      queue.append(word)
      break

  if queue:
    print("NO")
  else:
    print("YES")


