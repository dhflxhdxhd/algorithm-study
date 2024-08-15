#코딩테스트 연습
#월간 코드 챌린지 시즌1
#내적

def solution(a,b):
    inner = 0
    for i in range(len(a)):
        inner += a[i]*b[i]

    return inner

def solution(a,b):
    answer = sum([x*y for x,y in zip(a,b)])

    return answer