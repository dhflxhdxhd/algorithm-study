# 방법 1
n,k = map(int,input().split())
queue = [i+1 for i in range(n)]


idx = 0
print("<", end="")
for i in range(n,0,-1):
    idx = (idx + (k-1)) % i

    if len(queue) > 1:
        print(queue.pop(idx), end=", ")
    else:
        print(queue.pop(idx), end="")

print(">")


# 방법 2
from collections import deque

n, k = map(int, input().split())
list = [i+1 for i in range(n)]

queue = deque(list)
ans = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())

    ans.append(queue.popleft())


print("<", end = "")
for i in range(n-1):
    print(ans[i], end=", ")

print(f"{ans[-1]}>")











