import math

n = input("digite o valor n : ")

for i in range(int(n)):
    for j in range(int(n)):
        print(f"{j+1}",end="")
    print("\n")