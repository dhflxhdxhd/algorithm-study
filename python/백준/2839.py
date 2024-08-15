#설탕 배달
n = int(input())
num = 0
# if n%3 != 0:
#     num = -1
# else:
#     num = n//5
#     n -= num*5
#     num += n//3
#     n -= (n//3)*3
#     if n != 0:
#         num += 1

# print(num)

while n != 0:
    if n%5 == 0:
        num += n//5
        break 
    n -= 3 
    num += 1

    if n != 0 and n < 3:
        num = -1
        break

print(num)

