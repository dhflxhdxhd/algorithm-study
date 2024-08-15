#큐

import sys

n = int(sys.stdin.readline())
queue = []
for i in range(n):
    say = sys.stdin.readline().split()

    if say[0] == "push":
        queue.append(say[1])
    elif say[0] == "pop":
        if(queue != []):
            print(queue.pop(0))
        else:
            print(-1)
    elif say[0] == "size":
        print(len(queue))
    elif say[0] == "empty":
        if(queue == []): print(1)
        else: print(0)
    elif say[0] == "front":
        if(queue == []) : print(-1)
        else: print(queue[0])
    elif say[0] == "back":   
        if(queue == []): print(-1)
        else: print(queue[-1])
