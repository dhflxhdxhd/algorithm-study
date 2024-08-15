# def solution(numbers):
#     answer = 0
#     numbers.sort()
#     arr = [0]*10

#     for n in numbers:
#         arr[n] += 1

#     for i,a in enumerate(arr):
#         if a == 0:
#             answer += i

#     return answer

def solution(numbers):
    answer = 0
    numbers.sort()

    for i in range(0,10):
        if i not in numbers:
            answer += i

    return answer
numbers = [5,8,4,0,6,7,9]
solution(numbers)