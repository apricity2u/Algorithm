import sys
input = sys.stdin.readline

N = int(input())

sales_info = dict()

for _ in range(N):

  name = input()

  if name not in sales_info:
    sales_info[name] = 1
  else :
    sales_info[name] += 1

best_seller_book = ""
best_seller_count = 0

for name, count in sales_info.items():

  if count > best_seller_count:
    best_seller_book = name
    best_seller_count = count

  elif count == best_seller_count and name < best_seller_book:
    best_seller_book = name
    best_seller_count = count

print(best_seller_book)