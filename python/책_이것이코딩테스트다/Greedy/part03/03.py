# 문자열 뒤집기
string = input()

result = [0,0]

if string[0] == '0':
    result[0]  += 1
else: 
    result[1] += 1
    
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        if string[i] == '0':
            result[0] += 1
        else:
            result[1] += 1

print(min(result))
        