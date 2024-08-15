# 수행 시간이 길게 소요된다. 

def solution(number, k):
    # number 문자열 형식
    # k 제거할 수의 개수
    
    answer = ''
    number = list(map(int, list(number))) # number=[1,9,2,4]
    
    for i in range(k):
        max_num = max(number) # max_num => integer
        number.remove(max_num)

        answer += str(max_num)
        print(answer)
    

    return answer

solution("1924",2)
