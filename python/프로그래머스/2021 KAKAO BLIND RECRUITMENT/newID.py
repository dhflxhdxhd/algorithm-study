# 정규식을 쓰면 더 간단하게 할 수 있을 듯.

from collections import deque

def solution(new_id):
    # 1단계
    new_id = new_id.lower() # 대문자 -> 소문자
    
    queue = deque([])

    for idx in range(len(new_id)):
        if len(queue) == 15:
            break

        # 2단계 & 3단계
        if new_id[idx].islower() or new_id[idx].isdigit() or new_id[idx] == "-" or new_id[idx] == "_" or new_id[idx] == ".":
            if new_id[idx] == ".":
                if queue and queue[-1] != ".":
                    queue.append(new_id[idx])
            else:
                queue.append(new_id[idx])

    if len(queue) == 0:
        queue.append("a")

    if queue:
        if queue[-1] == ".":
            queue.pop()
   
    if len(queue) < 3:
        last = queue[-1]
        num = 3 - len(queue)

        for i in range(num):
            queue.append(last)
        
    return list(queue)
    
print("".join(solution(new_id)))      
        

