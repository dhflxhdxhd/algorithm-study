# ver2

n=input() # 입력 a1 (열-행)
row = int(n[1]) # 행
# 열, ord(c)는 문자의 아스키코드 값을 돌려주는 함수
col = int(ord(n[0]))-int(ord('a'))+1 

#move_types -> move_dx, move_dy
move_dx = [-2,-1,1,2,2,1,-1,-2] # 행
move_dy = [-1,-2,-2,-1,1,2,2,1] # 열

count = 0

for i in range(len(move_dx)):
    next_row = row + move_dx[i]
    next_col = col + move_dy[i]

    # matrix 8X8을 벗어나지 않는다면
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)
