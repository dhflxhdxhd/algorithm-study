#BFS 너비우선탐색
#가까운 노트부터 탐색
#큐 자료구조 사용

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start]) #deque()이용하여 queue 선언
    visited[start] = True #시작 노드 방문처리

    while queue: # queue가 빌 때까지 반복
        v = queue.popleft() # 가장 먼저 넣은 노드부터 선택
        print(v,end=" ")
        
        for i in graph[v]: # 선택한 노드에 인접한 노드들 탐색
            if not visited[i]: #인접 노드 중 방문하지 않은 노드가 있다면
                queue.append(i) # queue에 넣음
                visited[i] = True # 그리고 방문처리

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

bfs(graph,1,visited)