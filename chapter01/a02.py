# 入力
# こんな入力のやり方すぐ忘れるだろこれ
N, X = map(int, input().split())
A = list(map(int, input().split()))
resultFlag = False

# 単純に全探索すれば良さそう
for i in range(N):
  if A[i] == X:
    resultFlag = True
  
if (resultFlag):
  print('Yes')
else:
  print('No')
