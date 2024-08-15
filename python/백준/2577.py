
num = 1
for i in range(3):
    i = int(input())
    num *= i

cal = list(str(num))

for i in range(0,10):
    print(cal.count(str(i)))