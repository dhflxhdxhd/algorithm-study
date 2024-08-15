import sys
n = int(sys.stdin.readline())
list = []


for i in range(n):
    say = sys.stdin.readline().split()
    if say[0] == "push":
        list.append(say[1])
    elif say[0] == "pop":
        if(len(list) == 0):
            print(-1)
        else:
            print(list.pop())
    elif say[0] == "size":
        print(len(list))
    elif say[0] == "empty":
        if(len(list)== 0):
            print(1)
        else: print(0)
    elif say[0] == "top":
        if(len(list) != 0):
            print(list[-1])
        else: print(-1)
