# 3장/16.연구소
# 빈칸 0 벽 1 바이러스 2
import copy
n,m = map(int,input().split())

# 연구소 그래프 생성
lab = []
for i in range(n):
    lab.append(list(map(int,input().split())))
 
# 벽 세우기
def makeWall(count):
    if count == 3:
        graph = bfs()
        countZero(graph)
        return 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(count+1);
                lab[i][j] = 0
    
# 바이러스 퍼뜨리기
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs():
    queue = deque()
    testLab = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if testLab[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]

            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m :
                continue

            if testLab[nextX][nextY] == 0:
                testLab[nextX][nextY] = 2
                queue.append((nextX,nextY))

    return testLab

maxCount = 0
def countZero(graph):
    global maxCount;
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1

    maxCount = max(maxCount,count)

makeWall(0)
print(maxCount)