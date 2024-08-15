stack = []

while True:
    string = input()
    if string == ".":
        break

    for s in string:
        check = True

        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                check == False
               
                break
        elif s == "]":

    if stack :
        check = False

if check == True:
    print("yes")
else:
    print("no")