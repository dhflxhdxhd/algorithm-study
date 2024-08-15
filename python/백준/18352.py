# 그래프 이론
# 그래프 탐색
# 너비 우선 탐색
# 다익스트라
input_data = list(map(int,input().split()))

n = input_data[0]
m = input_data[1]
k = input_data[2]
x = input_data[-1]

graph = [[] for _ in range(n+1) ]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

from collections import deque

visited = [] * (???????????)
def bfs(start,visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        if graph[v]:
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True