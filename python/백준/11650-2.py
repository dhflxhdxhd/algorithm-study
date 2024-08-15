import sys

n = int(input())
data = [sys.stdin.readline() for _ in range(n)]

data.sort(key = lambda x:tuple(map(int,x.split())))

# print(data)
print("".join(data))
