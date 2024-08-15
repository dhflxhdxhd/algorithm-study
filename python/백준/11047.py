#그리디 알고리즘
n,k = map(int,input().split())
AI = [int(input()) for _ in range(n)]
AI.sort(reverse=True)
cnt = 0
for a in AI:
    if a <= k:
        cnt += k // a
        k %= a

print(cnt)