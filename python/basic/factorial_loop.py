#반복적으로 구현
def fac_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

print(fac_loop(3))