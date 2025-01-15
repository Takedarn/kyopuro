# input
N, X = map(int, input().split())
A = list(map(int, input().split()))

# search
l = 0
r = N

while True:
    m = (l + r) // 2
    if A[m] == X:
        print(m + 1)
        break
    elif A[m] < X:
        l = m
    elif A[m] > X:
        r = m