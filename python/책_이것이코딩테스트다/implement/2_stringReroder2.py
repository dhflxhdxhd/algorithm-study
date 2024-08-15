# isalpha함수는 문자열이 문자가 아닌지를 True, False로 리턴
# isdigit함수는 문자열이 숫자가 아닌지를 True, False로 리턴

import time
start_time = time.time()
s = input()
string = []
num = 0

for i in s:
    if i.isalpha():
        string.append(i)
    else:
        num += int(i)

string.sort()

# join : 리스트 -> 문자열
print(''.join(string),end="")
print(num)

end_time = time.time()
print("time:",end_time-start_time)



