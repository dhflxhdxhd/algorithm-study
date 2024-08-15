#bfs
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[v]:
                queue.append(i)
                visited[i] = True
                


com = int(input())
net = int(input())
graph = [[]*com for _ in range(com+1)]

for i in range(net):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (com+1)
bfs(graph,1,visited)
print(visited)