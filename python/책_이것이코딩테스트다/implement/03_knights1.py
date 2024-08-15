n=input() # 입력 a1 (열-행)
# 행
row = int(n[1]) 
# 열
# ord(c)는 문자의 아스키코드 값을 돌려주는 함수
col = int(ord(n[0]))-int(ord('a'))+1 

move_types = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count = 0

for move in move_types:
    next_row = row + move_types[0]
    next_col = col + move_types[1]

    # matrix 8X8을 벗어나지 않는다면
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)
