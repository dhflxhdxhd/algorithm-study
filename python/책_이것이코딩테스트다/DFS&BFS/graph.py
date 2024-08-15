#그래프 
INF = 999999999

#1. 인접행렬 방식
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

#2. 인접리스트방식
graph = [[] for_in range(3)]

# 노드 0에 연결된 노드 정보(노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))