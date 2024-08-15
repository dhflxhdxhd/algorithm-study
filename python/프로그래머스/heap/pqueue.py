import heapq

def solution(operations):
    answer = []

    for op in operations:
        a,b = op.split()
        if a == "I":
            heapq.heappush(answer,int(b))
        else:
            if len(answer) > 0:
                if b == '1':
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                else:
                    heapq.heappop(answer)

    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1,answer)[0], answer[0]]

operations = ["| 16", "D 1"]
print(solution(operations))