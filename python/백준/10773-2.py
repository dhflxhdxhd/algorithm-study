n = int(input())
a = []
result = 0
for i in range(n):
    num = int(input())
    if num != 0 :
        a.append(num)
        result += num
    else:
        result -= a[-1]
        a.pop()
        
print(result)

