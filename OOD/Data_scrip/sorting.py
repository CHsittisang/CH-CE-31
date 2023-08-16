import random

def sorting(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                

rnddat = [random.randint(1, 1000) for i in range(0, 100)]
sorting(rnddat)
print(rnddat) 

