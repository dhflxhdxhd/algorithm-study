# 코딩테스트 연습
# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기

def solution(numbers):
    ans = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            ans.add(numbers[i]+numbers[j])

    answer = list(ans)
    answer.sort()
    return answer

print(solution([5,0,2,7]))