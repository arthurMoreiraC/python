from math import *
aprox = int(input("digite a aprox: "))
1
s = 0

for k in range(aprox):
    s += 1/((k+1)**2)
s = sqrt(6*s)
print(f"aprox 1: {s}")

s = 0

for n in range(aprox):
    s += 8/((4*n + 1)*(4*n + 3))

print(f"aprox 2: {s}")
