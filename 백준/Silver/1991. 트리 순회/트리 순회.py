import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    parent, L, R = input().split()

    tree[parent] = [L, R]

pre_trail = []

def preorder(cur):
    pre_trail.append(cur)
    if tree[cur][0] != ".":
        preorder(tree[cur][0])
    if tree[cur][1] != ".":
        preorder(tree[cur][1])

in_trail = []

def inorder(cur):
    if tree[cur][0] != ".":
        inorder(tree[cur][0])
    in_trail.append(cur)
    if tree[cur][1] != ".":
        inorder(tree[cur][1])

post_trail = []

def postorder(cur):
    if tree[cur][0] != ".":
        postorder(tree[cur][0])
    if tree[cur][1] != ".":
        postorder(tree[cur][1])
    post_trail.append(cur)


preorder("A")
print("".join(pre_trail))
inorder("A")
print("".join(in_trail))
postorder("A")
print("".join(post_trail))
