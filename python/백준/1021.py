from collections import deque
n, m = map(int, input().split()) #큐의 크기 n / 수의 개수 m
idx = list(map(int, input().split())) # target의 위치 m개
queue = deque([i+1 for i in range(n)]) #[1,2,3,4,....,n]
count = 0 #2번, 3번 연산의 최솟값

for i in idx:
    target = i
    while True: # 1번 연산을 할 때까지 반복
        if queue[0] == target:
            queue.popleft()
            break
        else:
            if queue.index(target) < len(queue)/2:  #중심을 기준으로 중심값보다 작으면
                while queue[0] != target: # queue의 첫번째 값이 target이 될 때까지
                    queue.append(queue.popleft()) #2번 연산 수행
                    count += 1
            else:
                while queue[0] != target: 
                    queue.appendleft(queue.pop()) #3번 연산 수행
                    count += 1

print(count)