n= int(input())
plans = input().split()

# 동서남북 (R,L,U,D)
dx = [0,0,-1,1] #행
dy = [1,-1,0,0] #열
move = ["R","L","U","D"]
x,y=1,1 # 시작 지점 설정

#  하나씩 확인
for plan in plans:
    # 좌표 이동
    for i in range(len(move)):
        if plan == move[i]:
            move_x = x + dx[i]
            move_y = y + dy[i]
    if move_x < 1 or move_x > n or move_y < 1 or move_y > n:
        continue
    
    x,y = move_x,move_y

print(x,y)


