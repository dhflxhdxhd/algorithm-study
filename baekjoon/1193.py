num = int(input())
line = 1

#line 번호와 해당 line의 num이 몇 번째에 있는지.
while num > line:
    num -= line
    line += 1

if line%2 == 0:
    a = num
    b = line+1-num
else:
    a = line+1-num
    b = num

print(f'{a}/{b}')