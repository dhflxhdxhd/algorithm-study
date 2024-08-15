# programmers 체육복 문제입니다.

# n 전체 학생 수
# lost 체육복을 도난당한 학생들의 번호가 담긴 배열
# reserve 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
# 체육수업을 들을 수 있는 학생의 최댓값 return
    
def solution(n, lost, reserve):
    answer =0
    
    common = set(lost)&set(reserve)
    lost = set(lost) - common
    reserve = set(reserve) - common
    
    for reserve_data in reserve:
        if reserve_data-1 in lost:
            lost.remove(reserve_data-1)
        elif reserve_data +1 in lost:
            lost.remove(reserve_data+1)
    
    answer = n-len(lost)
    return answer
