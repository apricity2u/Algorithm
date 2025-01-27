import sys
input = sys.stdin.readline

n = int(input())

my_dict = {}

for _ in range(n):
    name, status = input().split()

    my_dict[name] = status

my_list = []

for name, status in my_dict.items():
    
    if (status == "enter"):
        my_list.append(name)

sorted_list = sorted(my_list, reverse = True)

for name in sorted_list:
    print(name)