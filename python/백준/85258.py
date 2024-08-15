# 큐2
# 입력값이 많을 대는 sys.stdin.readline()을 적극 활용하자
# 삼항연산자를 사용하면 한 줄로 코드를 나타내기 쉽다. 
# 하지만 속도면에서는 오히려 저조한 편이고 쉽게 버그를 만들어낼 수 있다는 의견이 있음. 
# 또한 오히려 한 줄로 나타내는 방식이 가독성을 떨어뜨린다고 여김. 

from collections import deque
import sys

queue = deque([])

n = int(input())
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[-1]))
    
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        print(0 if queue else 1)
        
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)

    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)
