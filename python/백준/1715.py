#카드 정렬하기
#시간초과
n =  int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


result = 0
while len(arr) != 1:
    arr.sort()
    one = arr.pop(0)
    two = arr.pop(0)
    sum = one + two
    result += sum
    arr.append(sum)

print(result)

    