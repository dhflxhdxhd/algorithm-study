# python 큐모델 사용하기

import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
cnt = 0
for i in range(n):
    say = sys.stdin.readline().split()

    if say[0] == "push":
        queue.append(say[1])
        cnt += 1
    elif say[0] == "pop":
        if(cnt != 0):
            print(queue.popleft())
            cnt -= 1
        else:
            print(-1)
    elif say[0] == "size":
        print(cnt)
    elif say[0] == "empty":
        if(cnt == 0): print(1)
        else: print(0)
    elif say[0] == "front":
        if(cnt == 0) : print(-1)
        else: print(queue[0])
    elif say[0] == "back":   
        if(cnt == 0): print(-1)
        else: print(queue[-1])
