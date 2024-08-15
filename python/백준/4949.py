
while True:
    string = input()
    if string == ".":
        break
    stack = []
    check = True    
    for i in string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":  
            if len(stack) > 0 and  stack[-1] == "(":
                stack.pop()
            else:
                check = False 
        elif i == "]" :
            if len(stack) > 0 and  stack[-1] == "[":
                stack.pop()
            else:
                check = False 
    if len(stack) > 0:
        check = False
    
    if check:
        print("yes")
    else:
        print("no")


