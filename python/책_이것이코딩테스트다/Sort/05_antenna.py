#18310
n = int(input())
locate = list(map(int,input().split()))

locate.sort()

print(locate[(n-1)//2]) # 중간값



