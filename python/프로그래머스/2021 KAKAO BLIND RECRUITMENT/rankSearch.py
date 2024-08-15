# 순위 검색


def solution(info, query):
    info_list = [([] for i in range(5)) for i in range(len(info))]
    query_list = [([] for i in range(5)) for i in range(len(info))]
    
    for i in range(len(info)):
        info_list[i] = info[i].split(" ")

    for j in range(len(query)):
        query_list[j] = query[j].split(" ")

    fo
    for x in range(len(info_list)):
        for y in range(5):
            if info_list[x][y] == query_list[x][y]:
                


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))





# 순위 검색
# 핵심 :  [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# -> { 조건 : 점수 } 형태의 dict 
from itertools import combinations

def solution(info, query):
    info_dict = {}
    
    for i in range(len(info)):
        info_list = info[i].split()
        ikey = info_list[:-1] # 조건
        ivalue = info_list[-1] # 점수
        
        for j in range(5):
            print(j)
            for c in combinations(ikey,j):
                tmp = "".join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(ivalue))
                else:
                    info_dict[tmp] = [int(ivalue)]


    [info_dict[k].sort() for k in info_dict]
    print(info_dict)

    for q in query:
        query_list = q.split()
        qkey = query_list[:-1]
        qvallue = query_list[-1]
        
        while 'and' in qkey :
            qkey.remove('and')

        while '-' in qkey:
            qkey.remove('-')

        qkey = ''.join(qkey)

        if qkey in info_dict:
            score = info_dict[qkey]
            if score:
                print("score", score)
  

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]





#solution(info,query)