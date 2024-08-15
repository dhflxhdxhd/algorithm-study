n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

# arr = sorted(arr, key = lambda data : (data[1], data[0]))

arr.sort(key=lambda data : (data[1],data[0]))

for data in arr:
    print(data[0],data[1])