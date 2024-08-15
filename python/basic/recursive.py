def recursive_func(i):
    #재귀함수에서는 무한궤도에 빠지지 않게 종료조건***
    if i == 10:
        return

    print("재귀함수 호출")
    recursive_func(i+1)

recursive_func(1)