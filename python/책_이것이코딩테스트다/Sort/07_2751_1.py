#백준 2751
import sys
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for a in arr:
    print(a)