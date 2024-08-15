# 바로 이전에 작업을 완료한 시간(start)보다 크고 현재 시점(now)보다 작으면 현재 시점에서 처리할 수 있는 작업이 된다.
# 현재 시점에서 처리할 수 있는 작업을 heap에 저장한다. 
# 이 때 소요시간을 기준으로 최소힙을 사용하기 때문에 heap을 저장할 때 [작업 소요 시간, 작업 요청 시간]으로 저장한다. 
# heap의 길이가 0보다 크다면 처리할 작업이 있는 경우이므로, 작업 요청시간부터 종료시간까지 계산하고 다음 작업으로 넘어갈 수 있도록 start와 now값을 바꿔준다. 
# heap의 길이가 0이라면 처리할 작업이 없는 경우 이므로 현재 시점을 다음 시간으로 넘어가기 위해 now에 1을 더한다. 
# 마지막으로 평균시간을 return한다. 

# 현재 시점에서 처리할 수 있는 작업들을 힙에 넣고, 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업을 처리할 때까지 반복. 
# 힙에 push를 할 때에는 작업의 소요시간 기준으로 최소힙이 만들어져야하므로 jobs 요소의 위치를 바꿔서 넣어준다.
# 현재 시점에서 처리할 수 있는 작업인지 판별하는 조건 : 작업의 요청시간이 바로 이전에 완료한 작업 시작 시간(start)보다 크고 현재 시점(now)보다 작아야함.
# 만약 현재 처리할 수 있는 작업이 없다면, 남아있는 작업들의 요청시간이 아직 오지 않은 것이기 때문에 현재 시점(now)를 하나 올려준다. 
import heapq

def solution(jobs):
    answer,now,cnt = 0,0,0 
    start = -1
    heap = []

    while cnt < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap,[j[1], j[0]])

        # 처리할 작업이 있는 경우
        if len(heap) > 0:
            cnt += 1
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1]) # 작업 요청시간부터 종료시간까지의 시간계산
        else: # 처리할 작업 X
            now += 1 
    return int(answer/len(jobs))

jobs = [[0,3], [1,9], [2,6]]
print(solution(jobs))
    
    