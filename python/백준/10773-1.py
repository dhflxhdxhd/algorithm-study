n = int(input())
a = []
result = 0
for i in range(n):
    num = int(input())
    if num != 0 :
        a.append(num)
    else:
        a.pop()

result = 0   
for  i in range(len(a)):
    result += a[i]
print(result)

