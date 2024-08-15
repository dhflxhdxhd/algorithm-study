
string = input()
count = 2

while string != "Was it a cat I saw?":
    
    for i in range(0,len(string),count):
        print(string[i], end="")

    print("")
    string = input()
    count += 1
   
    
    
    




  
    



