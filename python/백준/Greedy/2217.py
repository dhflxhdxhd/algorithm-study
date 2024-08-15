# 2217. 로프

n = int(input())
rope = []
result = []

for i in range(n):
    rope.append(int(input()))

rope.sort()

for r in rope:
    result.append(r*n)
    n -= 1

print(max(result))