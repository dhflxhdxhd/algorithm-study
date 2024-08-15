#2751
#퀵정렬 O(nlogn)
#메모리초과
import sys
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

def quick_sort(arr):
    # 종료조건 : 부분 리스트들이 더이상 분할이 불가능할 때까지. > 리스트의 크기가 0이나 1이되면 종료.
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left_arr = [x for x in tail if x <= pivot]
    right_arr = [x for x in tail if x > pivot]

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
    
arr = quick_sort(arr)

for a in arr:
    print(a)
    