from time import time 
from math import sin, cos

start = time()

temp = 0 
for i in range(10000000):
    ret = sin(1) / cos(1)
    temp = ret

for i in range(10000000):
    ret = temp + i

end = time()

print(f'value of equation w/o loop jamming: {ret}')
print(f'time taken w/o loop jamming: {end - start}')

print()

start = time()

equation = sin(1) / cos(1)
for i in range(10000000):
    ret = equation + i

end = time()

print(f'value of equation w/ loop jamming: {ret}')
print(f'time taken w/ loop jamming: {end - start}')
