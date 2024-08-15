import sys

def cnt_BW(new_board):
    w_renew = 0
    b_renew = 0

    # 8*8로 자른 new_board에 대하여
    # W로 시작하는 경우
    for x in range(8):
        for y in range(8):
            if((x%2 == 0 and y%2 ==0) or (x % 2 ==1 and y%2==1)):
                if new_board[x][y] != "W":
                    w_renew += 1
                
            elif ((x%2 == 0 and y%2 ==1) or (x % 2 ==1 and y%2==0)):
                if new_board[x][y] != "B":
                    w_renew += 1

    # B로 시작하는 경우
    for x in range(8):
        for y in range(8):
            if((x%2 == 0 and y%2 ==0) or (x % 2 ==1 and y%2==1)):
                if new_board[x][y] != "B":
                    b_renew += 1
                
            elif ((x%2 == 0 and y%2 ==1) or (x % 2 ==1 and y%2==0)):
                if new_board[x][y] != "W":
                    b_renew += 1                   

    return min(w_renew, b_renew)

board = []
m,n = map(int, input().split())
# board 입력받기
for _ in range(m):
    board.append([i for i in sys.stdin.readline()][:-1])

min_renew = 1e9
renew = 0
for row in range(m-7):
    for col in range(n-7):
        # 8*8 board로 자르기.
        new_board = [new_row[col:col+8] for new_row in board[row:row+8]]
        renew = cnt_BW(new_board)
        min_renew = min(min_renew, renew)


print(min_renew)

