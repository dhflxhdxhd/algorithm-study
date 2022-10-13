from collections import deque
import sys

t = int(input())

for i in range(t):

    command = sys.stdin.readline()
    n = int(input())
    nums = sys.stdin.readline()[1:-1].split(',')
    queue = deque(nums)
    
    if n == 0:
        queue = deque()
    else:
        queue = deque(nums)

    
    check = 1
    for cmd in command:
        if cmd == "R":
            queue.reverse()
        elif cmd == "D":
            if queue:
                queue.popleft()
            else:
                print("error")
                check = 0
                break

    if check == 1:
        print("["+",".join(list(queue))+"]")
 


