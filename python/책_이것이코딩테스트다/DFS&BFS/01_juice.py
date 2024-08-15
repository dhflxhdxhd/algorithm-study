#error
#세로가 n이고 가로가 m인데 왜지??????????????????????


n,m = map(int,input().split()) #세로 n 가로 m

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result = 0
for i in range(m):
    for j in range(n)):
        if dfs(i,j) == True:
            result += 1

print(result)