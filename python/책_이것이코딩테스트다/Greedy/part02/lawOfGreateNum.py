# 1. 가장 큰 수와 두 번째로 큰수를 저장. 
# 2. 가장 큰 수를 k번만큼 더한 후 두 번째로 큰 수를 한번 더하기 until 더해지는 총 횟수가 m이 될 때까지 
# 1. save the most biggest number and the second one
# 2. after adding the most biggest one k times, add the second one once until total count is m

n,m,k = map(int, input().split())
data = list(map(int,input().split()))
result = 0

data.sort()
first_data = data[n-1]
second_data = data[n-2]

while True:
    for i in range(k):
        if m != 0:
            result += first_data
            m -= 1
        else:
            break

    if m == 0:
        break
    result += second_data
    m -= 1

print(result)


