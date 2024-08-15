import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    # 두 원의 중심 사이의 거리
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if d == 0:    # 두 원의 원점(중심)이 같을 때
        if r1 == r2: # 원의 크기 동일할 때 > 무수히 많은 접점
            print(-1)
        else:     
            print(0) # 동심원
    else:         # 두 원의 원점(중심)이 다를 때
        if r1+r2 == d or abs(r2-r1) == d: # 접하는 경우
            print(1)
        elif ((abs(r1-r2) < d) and (d < r1+r2)): #두 점에서 만나는 경우
            print(2)
        else: 
            print(0)