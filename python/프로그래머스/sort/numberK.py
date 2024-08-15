# def solution(array, commands):
#     num = []
#     length = len(commands)

#     for i in range(length):
#         list = sorted(array[commands[i][0]-1:commands[i][1]])
#         num.append(list[commands[i][2]-1])

#     return num
        
        
def solution(array, commands):
    num = []

    for command in commands:
        i,j,k = command
        num.append(sorted(array[i-1:j])[k-1])

    return num
        
        
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1]]
print(solution(array,commands))