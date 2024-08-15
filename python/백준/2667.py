n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


def dfs(graph,x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 2
        cnt += 1
        dfs(graph,x-1, y)
        dfs(graph,x+1, y)
        dfs(graph,x,y-1)
        dfs(graph,x,y+1)
        return True
    return False

result = 0
cnt = 0
num = []
for i in range(n):
    for j in range(n):
        if dfs(graph,i,j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)     
for i in num:
    print(i)
