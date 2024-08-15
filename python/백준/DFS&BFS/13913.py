# 13913. 숨바꼭질 4
from collections import deque
n,k = map(int,input().split())
MAX = 10**5
sec = [-1] * (MAX+1)
visited = [0] * (MAX+1)
path = []

def bfs(start) :
    queue = deque([start])
    sec[start] = 0
    visited[start] = start 
    while queue:
        v = queue.popleft()
        if v == k:
            node = v
            while node != start:
                path.append(node)
                node = visited[node]
            path.append(start)
            return sec[v]
        
        moveDirection = [v-1, v+1, v*2]

        for direction in moveDirection:
            if 0 <= direction <= MAX and sec[direction] == -1:
                queue.append(direction)
                sec[direction] = sec[v] + 1
                visited[direction] = v

result = bfs(n)
print(result)
print(*path[::-1])