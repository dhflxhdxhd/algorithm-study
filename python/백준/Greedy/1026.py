# 1026. 보물

n = int(input())
aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))
result = 0

aArr.sort()
bArr.sort(reverse=True)

for i in range(n):
    result += aArr[i] * bArr[i]

print(result)
