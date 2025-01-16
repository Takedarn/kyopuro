# check
def check(x, N, K, A):
    total = 0
    for i in range(N):
        total += x // A[i]
    return total >= K  # TrueかFalseを返す

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索
left = 0
right = 10 ** 9
while left < right:
    mid = (left + right) // 2
    if check(mid, N, K, A):
        right = mid
    else:
        left = mid + 1

# 回答
print(left)