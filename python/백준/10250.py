# 10250번: ACM호텔
# 문제 풀이 
# H,W,N : 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
# if N <= H*W 
# N%H == 0 N//H <- 방 번호 X && N%H == 0, H <- 층 수 Y
# N%H > 0, N//H+1 <- 방 번호 X  && N%H > 0, N%H <- 층 수 Y

T = int(input())

for t in range(T):
    h,w,n = map(int,input().split())

    if n <= h*w:
        if n%h == 0:
            x = n//h
            y = h
        else:
            x = n//h + 1
            y = n%h
        
        #방법 1
        num = y*100 + x 
 
    #방법 2
    # if x<10:
    #     num = str(y)+ '0'+str(x) 
    # else:
    #     num = str(y) + str(x)   
    print(num)