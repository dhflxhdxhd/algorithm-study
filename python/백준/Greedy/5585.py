# 5585.거스름돈

price = int(input())
coin = [500, 100, 50, 10, 5, 1]
change = 1000 - price

count = 0
for c in coin:
    num = change // c
    count += num
    change -= c * num

    if change == 0:
        break

print(count)
