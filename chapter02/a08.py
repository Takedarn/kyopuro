# 入力する
H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Z = [[0] * (W + 1) for _ in range(H + 1)]

# 入力（後半）
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 横方向に累積和をとる
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j - 1] + X[i - 1][j - 1]

# 縦方向に累積和をとる
for j in range(1, W + 1):
    for i in range(1, H + 1):
        Z[i][j] += Z[i - 1][j]

# 答えを求める
for A, B, C, D in queries:
    result = Z[C][D] + Z[A - 1][B - 1] - Z[A - 1][D] - Z[C][B - 1]
    print(result)