import heapq


def dijkstra(graph, start):
    distances = { node: float('inf') for node in graph }
    distances[start] = 0
    
    queue = []
    
    heapq.heappush(queue, [distances[start], start]) # [비용, 노드]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
            
        for new_node, new_distance in graph[current_node].itmes():
            distance = current_distance + new_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
                
                
    return distances