# 3장/17.경쟁적 전염
from collections import deque
n, k = map(int, input().split())
examiner = []
data = []
sec = 0

for i in range(n):
    examiner.append(list(map(int, input().split())))
    for j in range(n):
        if examiner[i][j]:
            data.append([examiner[i][j], (i, j), sec])

data = sorted(data, key=lambda x: (x[0], x[2]))


targetSec, targetX, targetY = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque(data)
    while queue:
        virusNum, loc, sec = queue.popleft()

        if sec == targetSec:
            break

        for i in range(4):
            nextX = loc[0] + dx[i]
            nextY = loc[1] + dy[i]

            if nextX < 0 or nextX >= n or nextY < 0 or nextY >= n:
                continue

            if examiner[nextX][nextY] == 0:
                examiner[nextX][nextY] = virusNum
                queue.append([virusNum, (nextX, nextY), sec+1])

    return examiner


bfs()
result = examiner[targetX-1][targetY-1]
print(result)
