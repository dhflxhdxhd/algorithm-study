# 곱하기 혹은 더하기

num=input()
result = int(num[0])

for i in range(0,len(num)-1):
    if int(num[i]) == 0 or int(num[i]) == 1:
        result += int(num[i+1])
    else:
        result *= int(num[i+1])
print(result)