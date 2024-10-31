N = int(input())

for x in range(9, -1, -1):  
    print((N >> x) & 1, end='')  

print("") 
