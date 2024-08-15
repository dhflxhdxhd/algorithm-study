# 빠른 입출력

import sys
n = int(input())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

list.sort()

for i in range(len(list)):
    print(list[i])