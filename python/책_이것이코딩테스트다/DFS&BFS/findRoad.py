# 3장/15.특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

count = [0]*(n+1)
visited = [False]*(n+1)
check = False

def bfs(x, visited):
    queue = deque()
    queue.append(x)

    while queue:
        v = queue.popleft()
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count[i] = count[v] + 1

bfs(x, visited)

for i in range(n+1):
    if count[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
