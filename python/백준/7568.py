#덩치
#브루트포스

n = int(input())

score = []
person = [ list(map(int,input().split())) for i in range(n)]

# for i in range(n):
#  x, y = map(int,input().split())
#  person.append((x,y))

for i in range(n):
    cnt = 1
    for j in range(n):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            cnt += 1
    score.append(cnt)

for s in score:
    print(s, end=" ")

