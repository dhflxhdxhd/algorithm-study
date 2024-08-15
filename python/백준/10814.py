n = int(input())

arr = [list(input().split()) for _ in range(n)]

arr.sort(key = lambda data:(int(data[0])))

for data in arr:
    print(data[0],data[1])
