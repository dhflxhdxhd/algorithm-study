#소인수분해
n = int(input())
num = 2
while True:
    if n % num == 0:
        print(num)
        n //= num
    elif n == 1:
        break
    else:
        num += 1