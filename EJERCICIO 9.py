número = int(input("Introduce un número entero"))

for i in range(1, número+1, 2):
    for j in range(i, 0, -2): 
        print(j, " ") 
    print("") 