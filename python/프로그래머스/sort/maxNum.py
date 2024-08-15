def solution(numbers):
    snumbers = list(map(str, numbers))
    snumbers.sort(key = lambda num : num*3 , reverse=True)

    maxn = "".join(snumbers)
    return maxn

numbers = [3,30,34,5,9]
print(solution(numbers))