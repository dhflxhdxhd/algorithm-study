import heapq

def solution(operations):
    answer = []

    for op in operations:
        a,b = op.split()
        if a == "I":
            answer.append(int(b))
        else:
            if len(answer) > 0:
                if b == '1':
                    answer.pop()
                else:
                    answer.pop(0)

        answer.sort()
    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer), min(answer)]
    return answer

operations = ["| 16", "D 1"]
print(solution(operations))