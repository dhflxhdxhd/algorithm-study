n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda data: (data[0],data[1]))

for data in arr:
    print(data[0],data[1])