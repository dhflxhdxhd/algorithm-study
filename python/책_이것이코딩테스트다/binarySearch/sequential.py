# 순차탐색
# 가장 앞에 있는원소부터 하나씩 확인해야한다.
# 최악의 경우 O(N)

def sequential(n,arr):
    for i in range(n):
        if target == arr[i]:
            return i+1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

arr = []
for _ in range(n):
    arr.append(input())

print(sequential(n,arr))