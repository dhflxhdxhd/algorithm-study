
s = input()
string = []
num = 0

for i in range(len(s)):
    if ord(s[i]) >= 65:
        string.append(s[i])
    else:
        num += int(s[i])

string.sort()

for i in range(len(string)):
    print(string[i],end="")

print(num)

# takes too much time
