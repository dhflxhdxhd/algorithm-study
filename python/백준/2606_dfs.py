#virus
#DFS

def dfs(graph,v,visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph,i,visited)



com = int(input())
net = int(input())
graph = [[]*com for _ in range(com+1)]

for i in range(net):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (com+1)

dfs(graph,1,visited)
print(cnt)
# print(visited.count(True)-1)