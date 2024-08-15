# 곱하기 혹은 더하기
# multiple or plus
# point: num값이 1보다 같거나 작으면 더한다. result값이 1보다 작거나 같으면 더한다.
s=input()
result = int(s[0])

if len(s)>=1 and len(s)<=20:
    for i in range(1,len(s)):
        num = int(s[i])
        if num<=1 or result <= 1:
            result += num
        else:
            result *= num

print(result)
