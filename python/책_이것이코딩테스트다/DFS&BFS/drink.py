# 음료수 얼려 먹기

n, m = map(int,input().split())

# 그래프 생성
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):

    # 예외
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if graph[x][y] == 0:
        # 방문 표시
        graph[x][y] = 2
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)

