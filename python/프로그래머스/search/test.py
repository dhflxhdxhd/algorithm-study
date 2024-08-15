def solution(answers):
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    check = [0,0,0]
    answer = []
    
    for i in range(len((answers))):
        if answers[i] == ans1[i%5]:
            check[0] += 1

        if answers[i] == ans2[i%8]:
            check[1] += 1

        if answers[i] == ans3[i%10]:
            check[2] += 1

    max_score = max(check)

    for i, ck in enumerate(check):
        if ck == max_score:
            answer.append(i+1)
    return answer

    
print(solution([1,3,2,4,2]))
    
            
        