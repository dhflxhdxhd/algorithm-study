N, M = map(int, input().split())  # N:주어진 수, M:수열의 길이
arr = []  # 출력 수열 넣을 리스트 (stack)
visited = [False] * (N+1)  # 방문체크 할 리스트

def dfs():
    # print(arr)
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        
        if visited[i]:  # 이미 방문했으면 건너뜀
            print(f'i = {i}')
            continue

        # 방문 안했으면 방문체크한 후, 출력 리스트에 넣고 다음 함수 호출
        visited[i] = True
        arr.append(i)
        dfs()  # 재귀
        arr.pop()  # 원상복귀 
        # print("pop")
        # print(arr)
        visited[i] = False

dfs()
