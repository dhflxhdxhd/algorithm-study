# 볼링공 고르기
n, m = map(int, input().split())
k = list(map(int, input().split()))
weightArray = [0]*10
count = 0

# 무게 별 볼링공 개수 세기
for weight in k:
    weightArray[weight] += 1

for i in range(m):
    n -= weightArray[i]
    count += weightArray[i] * n

    if n == 0:
        break

print(count)
