n = int(input())
stk = []

for _ in range(n):
    stk.append(int(input()))  

# num = 1
# arr = []

# for s in stk:
# for i in range(s):
#         if arr[-1] == s:
#         arr.pop()
#         print("-")
#         break
#         arr.append(num)
#         num += 1
#         print("+")

num = 1
arr = []
res = []
check = True
for s in stk:
    while num <= s:
        arr.append(num)
        res.append("+")
        num += 1

    if arr[-1] == s:
        arr.pop()
        res.append('-')

    else:
        check = False

if check:
    for r in res:
        print(r)
else:
    print("NO")

    
        

