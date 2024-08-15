coin = [500, 100, 50, 10]
money = int(input())
count = 0;

for c in coin : 
    count += money // c
    money -= c*(money//c)
    
    if money==0 :
        break
print(count)