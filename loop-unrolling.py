from time import time 

start = time()

array = [0] * 5

for i in range(10000000):
    for x in range(len(array)):
        array[x] = x

end = time()

print(f'resultant array w/o loop unrolling: {array}')
print(f'time taken w/o loop unrolling: {end - start}')

print()

start = time()

array = [0] * 5

for i in range(10000000):
    array[0] = 0
    array[1] = 1
    array[2] = 2
    array[3] = 3
    array[4] = 4

end = time()

print(f'resultant array w/ loop unrolling: {array}')
print(f'time taken w/ loop unrolling: {end - start}')

