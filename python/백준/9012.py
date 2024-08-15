n = int(input())

for _ in range(n):
    check = True
    stack = []
    data = input()
    
    for i in data:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                # 올바르지 않은 문자열일 때
                check = False
                break

    if not stack and check == True:
        print("YES")
    else:
        print("NO")
    
# n = int(input())
# cnt = 0

# def vps(data):
#     global cnt
#     for i in range(len(data)):
#         if  data[i] == '(':
#             cnt += 1
#         elif data[i] == ")":
#             cnt -= 1
#         elif cnt < 0:
#             return False

#     if cnt != 0:
#         return False
#     return True


# for _ in range(n):
#     data = sys.stdin.readline()
    
#     if vps(data):
#         print("YES")
#     else:
#         print("NO")

