#계수정렬 count sort
#메모리 초과 > 개수 제한시킴. 
import sys
n = int(input())

count = [0] * 10001

for _ in range(n):
    arr_num = int(sys.stdin.readline())
    count[arr_num] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)