# 3장/Q.18 괄호 변환

from collections import deque
w = input()

# 균형잡힌 괄호 문자열 u,v로 분리하기
def divideUV(string):
    sum = 0
    for i in range(len(string)):
        if string[i] == "(":
            sum += 1
        elif string[i] == ")":
            sum -= 1

        if sum == 0:
            u = string[:i+1]
            if i+1 < len(string) :
                v = string[i+1:]
            else:
                v = ""
        
        break
    return u,v

# 올바른 문자열 검사
def checkCorrect(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            stack.pop()
    return True

def converseBracket(w):
    if not w : return ""
    u,v = divideUV(w)
    print(u,v)
    if checkCorrect(u):
        result = u + converseBracket(v)
        return result
    else:
        temp = "("
        temp += converseBracket(v)
        temp += ")"
        middleU = u[1:-1]
        for mid in middleU:
            if mid == ")":
                temp += "("
            else:
                temp += ")"

        return temp

if checkCorrect(w) :
    print(w)
else:
    answer = converseBracket(w)
    print(answer) 