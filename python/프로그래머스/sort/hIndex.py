# def solution(citations):
#     answer = 0

#     citations.sort()
#     index = len(citations) // 2 

#     if len(citations) % 2 == 0:
#         h = citations[index - 1]
#     else:
#         h = citations[index]
#     return h

def solution(citations):
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)
citations = [3,0,6,1,5]
print(solution(citations))