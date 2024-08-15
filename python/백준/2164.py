# 카드 2
n = int(input())
from collections import deque

queue = deque([i+1 for i in range(n)])

while len(queue) > 1:
    queue.popleft()
    t = queue.popleft()
    queue.append(t)

print(queue[0])