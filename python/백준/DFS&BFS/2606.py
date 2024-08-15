# 2606. 바이러스
from collections import Counter

computer = int(input())
couple = int(input())
graph = [[]*computer for _ in range(computer+1)]

visited = [False]*(computer+1)

for i in range(couple):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 이중 리스트 정렬

def dfs(graph,v,visited):
    visited[v] = True;

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited);

dfs(graph,1,visited)

counter = Counter(visited)
print(counter[True]-1)
