#재귀
def fac_recursive(n):
    if n <= 1:
        return 1
    return n*fac_recursive(n-1)

print(fac_recursive(3))