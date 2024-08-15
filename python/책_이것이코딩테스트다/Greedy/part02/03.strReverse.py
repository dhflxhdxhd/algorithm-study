str = input()
count0 = 0
count1 = 0

if str[0] == '0':
    count1 += 1
else: 
    count0 += 1


for i in range(0, len(str)-1):
    if str[i] != str[i+1]:
        if str[i+1] == '1':
            count0 += 1
        else: 
            count1 += 1

print(min(count0, count1)) 