import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  k = int(input())
  words = list()
  flag = False

  for _ in range(k):
    word = input().strip()
    words.append(word)


  for i in range(k):

    for j in range(k):
      if i == j:
        continue

      new_word = words[i] + words[j]
      reverse_new_word = new_word[::-1]

      if new_word == reverse_new_word:
        print(new_word)
        flag = True
        break

    if flag:
      break
  
  if flag == False:
    print(0)