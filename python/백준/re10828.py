# import sys

# n = int(input())
# ans = []

# for _ in range(n):
#     say = sys.stdin.readline().split()
#     if (say[0] == "push"):
#         ans.append(say[1])
#     if (say[0] == "pop"):
#         if (len(ans) == 0) :
#             print(-1)
#         else: print(ans.pop())
#     if (say[0] == "size"):
#         print(len(ans))
#     if (say[0] == "empty"):
#         if (len(ans) == 0):
#             print(1)
#         else: print(0)
#     if (say[0] == "top"):
#         if (len(ans) == 0):
#             print(-1)
#         else:
#             print(ans[-1])


import sys

n = int(input())
ans = []
result = 0
for _ in range(n):
    say = sys.stdin.readline().split()
    if(say[0] == "push"):
        ans.append(say[1])
    if(say[0] == "pop"):
        result = -1 if len(ans) == 0 else ans.pop()
        print(result)
    if(say[0] == "size"):
        print(len(ans))
    if(say[0] == "empty"):
        result = 1 if len(ans) == 0 else 0
        print(result)
    if(say[0] == "top"):
        result = -1 if len(ans) == 0 else ans[-1]
        print(result)