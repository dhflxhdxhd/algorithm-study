#깊이 우선 탐색
#스택 -> 재귀
def dfs(graph,v,visited):
    visited[v] = True #현재 노드(v) 방문
    print(v, end=" ") 

    for i in graph[v]: #현재 노드와 연결된 노드들 순서대로
        if not visited[i]: # 방문 X ->
            dfs(graph,i,visited) # 방문(재귀)

#각 노드가 연결된 정보 리스트(2차원)
#0번부터
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

visited = [False] *9 #노드개수만큼 방문 정보 리스트 생성
dfs(graph,1,visited) #DFS함수 호출 / 가장 작은 노드부터