#통계학
#정렬

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

def average(arr):
    print(sum(arr)/len(arr))


print(arr[n//2])  

def mode(arr):
    print("mode")

def range_arr(arr):
    print(arr[-1] - arr[0])

average(arr)
mode(arr)
range_arr(arr)