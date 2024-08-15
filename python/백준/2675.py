n = int(input())

for i in range(n):
    cnt, word = input().split()
    for i in word:
        print(i*int(cnt),end="")
    print()
