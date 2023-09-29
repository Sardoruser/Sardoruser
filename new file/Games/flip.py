import random
import time

input("Starting")

flips = 0
heads= 0

while flips < 1000:
    
    
    if random.randint(0, 1) == 1:
        heads += 1#heads = heads + 1
    flips += 1 #flips = flips + 1
    
    if flips == 900:
        print("900 Flips and heads are "+str(heads))
        time.sleep(1)
    if flips == 100:
        print("100 Flips and heads are "+str(heads))
        time.sleep(1)
    if flips == 500:
        print("500 Flips and heads are "+str(heads))
        time.sleep(1)
print()
time.sleep(3)
print(flips, heads)