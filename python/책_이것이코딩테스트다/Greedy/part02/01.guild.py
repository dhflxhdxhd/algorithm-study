# 01 모험가 길드

n = int(input())
fear = list(map(int,input().split()))
count = 0;

fear.sort(reverse=True)

while fear:
    maxFear = fear[0];
    if len(fear) < maxFear:
        break;

    fear = fear[maxFear:]
    count += 1;


print(count)
