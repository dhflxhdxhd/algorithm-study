# 프린터
def solution(priorities, location):
    answer = []
    num_index = [i for i in range(len(priorities))]
    idx = 0
    
    while priorities:
        check = True
        num = priorities.pop(0)
        for p in priorities:
            if num < p:
                priorities.append(num)
                num_index.append(num_index.pop(0))
                check = False
                break
        if check:
            answer.append(num_index.pop(0))

    return answer.index(location) + 1

# def solution(priorities, location):
#     answer = []
#     num_loc = [i for i in range(len(priorities))]
 
#     while priorities:
#         if priorities[0] == max(priorities):
#             answer.append(num_loc.pop(0))
#             priorities.pop(0)
#         else:
#             priorities.append(priorities.pop(0))
#             num_loc.append(num_loc.pop(0))

#     return answer.index(location) + 1


print(solution([1,1,9,1,1,1],0))