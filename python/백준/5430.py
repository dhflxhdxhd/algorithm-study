from collections import deque
import sys

t = int(input())

for i in range(t):
    command = sys.stdin.readline()
    n = int(input())
    nums = sys.stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(nums)
    
    if n == 0:
        queue = deque()

    reverse = 0
    check = 1
    for cmd in command:
        if cmd == "R":
            reverse += 1
        elif cmd == "D":
            if queue:
                if reverse % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print("error")
                check = 0
                break

    if check == 1:
        if reverse % 2 == 1:
            queue.reverse()
        print("["+",".join(list(queue))+"]")
 