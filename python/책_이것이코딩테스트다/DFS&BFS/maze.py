# 미로 탈출

from collections import deque

n,m = map(int,input().split())

# 미로 생성
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # 상하좌우 이동 경우
        for i in range(4):
            nextX = x + dx[i] 
            nextY = y + dy[i]
    
            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
                continue

            if maze[nextX][nextY] == 0:
                continue

            if maze[nextX][nextY] == 1:
                maze[nextX][nextY] = maze[x][y] + 1
                queue.append((nextX,nextY));

    return maze[n-1][m-1]


print(bfs(1,1))

            
            
                

