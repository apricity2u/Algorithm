import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

max_tem = tmp = sum(nums[:K])

for idx in range(N-K):
  tmp += nums[idx+K] - nums[idx]
  max_tem = max(max_tem, tmp) 

print(max_tem)