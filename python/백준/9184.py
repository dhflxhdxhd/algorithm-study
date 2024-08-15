#9184. 신나는 함수 실행
MAX = 21
d = [[[0 for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    if d[a][b][c]:
        return d[a][b][c]
        
    if a < b and b < c :
        d[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a, b-1, c)
    else:
        d[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return  d[a][b][c]

# print(w(-1,7,18))

while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')