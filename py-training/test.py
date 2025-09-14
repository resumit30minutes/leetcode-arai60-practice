
# 基本的な入出力
from sys import stdin

a = stdin.readline().rstrip()
print(a.upper())

# 空白で分割
b, c = stdin.readline().rstrip().split()
print(b, c)
