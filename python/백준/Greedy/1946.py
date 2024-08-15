# 1946. 신입사원
import sys
n = int(input())
score = []
count = 0

for i in range(n):
    resume, interview = map(int,input().split())
    score.append([resume,interview])

score = sorted(score, key=lambda x:x[0])

for i in range(n):
    for j in range(n):
        if score[i][0] >= score[j][0]:
            count += 1
        elif score[i][1] >= score[j][1]:
            count += 1
        