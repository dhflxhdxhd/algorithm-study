#기능개발

# def solution(progresses, speeds):
#     # progress.sort(reverse=True)
#     # speeds.sort(reverse=True)
#     cost_day = []
#     for i in range(len(progresses)):
#         progresses[i] = 100 - progresses[i]
#         cost_day.append(progresses[i] // speeds[i])
#         if (progresses[i] % speeds[i]):
#             cost_day[i] += 1
    
#     answer = []
#     cnt = 1
#     current = cost_day[0]
#     for i in range(1,len(cost_day)):
#         if  current >=  cost_day[i]:
#             cnt += 1
#         else: 
#             answer.append(cnt)
#             cnt = 1
#             current = cost_day[i]
#     answer.append(cnt)
#     return answer

# print(solution([93,30,55],[1,30,5]))


import math

def solution(progresses, speeds):
    answer = []
    cnt = 1
    current = math.ceil((100-progresses[0]) / speeds[0])
    for i in range(1,len(progresses)):
        if  current >=  math.ceil((100-progresses[i]) / speeds[i]):
            cnt += 1
        else: 
            answer.append(cnt)
            cnt = 1
            current = math.ceil((100-progresses[i]) / speeds[i])
    answer.append(cnt)
    return answer

print(solution([93,30,55],[1,30,5]))