# version 2
# 가장 큰 숫자를 더하는 횟수를 구하기

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first_data = data[n-1]
second_data= data[n-2]
result = 0

# python 몫 "//"or int(a/b) 이용.
count = (m//(k+1)*k)+(m%(k+1))
result += count*first_data
result += (m-count)*second_data

print(result)

