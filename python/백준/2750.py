#삽입정렬
#1. 2번째 원소부터 시작
#2. 이전에 있는 원소들과 비교하여 작을 경우 swap

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
    
        else:
            break

for a in arr:
    print(a)